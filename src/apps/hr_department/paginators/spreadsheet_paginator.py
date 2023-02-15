from django_elasticsearch_dsl_drf.pagination import QueryFriendlyPageNumberPagination


class SpreadSheetPagination(QueryFriendlyPageNumberPagination):
    """Custom page number pagination."""

    def get_paginated_response_context(self, data):
        __data = super(
            SpreadSheetPagination,
            self
        ).get_paginated_response_context(data)
        __data.append(
            ('current_page', int(self.request.query_params.get('page', 1)))
        )
        __data.append(
            ('page_size', self.get_page_size(self.request))
        )
        return sorted(__data)
