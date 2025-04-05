# this is a file intended to configurate pagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagePagination(PageNumberPagination):
    # if we move to PageNumberPagination, we can see what we can change
    page_size = 3  # quantity of elems
    max_page_size = 10
    page_size_query_param = 'size'  # The client (for example, Postman or a browser) can specify how many elements to return on one page - via the ?size=... parameter in the URL.

    def get_paginated_response(self, data):  # It forms the final answer.
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': bool(self.get_previous_link()),  # to specify bool type, not a link
            'next': bool(self.get_next_link()),
            'data': data
        })
