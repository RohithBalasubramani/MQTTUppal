from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from django.apps import apps
from rest_framework import viewsets, filters
import pandas as pd
from django.core.cache import cache


class CustomDateTimeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_date_time = request.query_params.get("start_date_time")
        end_date_time = request.query_params.get("end_date_time")
        resample_period = request.query_params.get("resample_period")

        if start_date_time and end_date_time:
            queryset = queryset.filter(
                date_time__range=(start_date_time, end_date_time)
            )

        if resample_period:
            queryset = view.resample_data(queryset, resample_period)

        return queryset


# Custom Pagination Class
class CustomPagination(PageNumberPagination):
    page_size = 2000  # Adjust as needed
    page_size_query_param = "page_size"
    max_page_size = None  # Set a maximum page size if required


app_models = apps.get_app_config("main").get_models()

for model in app_models:
    class_name = f"{model.__name__}ViewSet"
    queryset = model.objects.order_by("-timestamp")
    serializer_class = globals()[f"{model.__name__}Serializer"]

    class DynamicViewSet(ReadOnlyModelViewSet):
        queryset = queryset
        serializer_class = serializer_class
        pagination_class = CustomPagination
        filter_backends = [CustomDateTimeFilter]  # Include the custom filter

        def get_object(self):
            queryset = self.get_queryset()
            pk = self.kwargs.get("pk")
            return get_object_or_404(queryset, pk=pk)

        def resample_data(self, queryset, resample_period):
            cache_key = f"resampled_data_{resample_period}"

            # Check if the data is already cached
            cached_data = cache.get(cache_key)
            if cached_data:
                return cached_data

            # Convert queryset to Pandas DataFrame
            df = pd.DataFrame(list(queryset.values()))

            # Convert 'timestamp' column to datetime type
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Set 'timestamp' column as the index
            df.set_index("timestamp", inplace=True)

            # Resample the data based on the provided period (e.g., 'D' for daily, 'H' for hourly)
            resampled_df = df.resample(resample_period).sum()

            # Reset the index to include the 'timestamp' column in the result
            resampled_df.reset_index(inplace=True)

            # Convert the Pandas DataFrame back to a queryset
            resampled_queryset = [dict(row) for _, row in resampled_df.iterrows()]

            # Cache the computed results
            cache.set(
                cache_key, resampled_queryset, timeout=None
            )  # Set timeout=None for indefinite caching

            return resampled_queryset

    locals()[class_name] = DynamicViewSet
