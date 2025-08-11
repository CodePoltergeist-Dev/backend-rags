# api/charts.py
try:
    from admin_charts.charts import Chart  # Optional dependency
except ImportError:  # Fallback stub to avoid runtime errors if package not installed
    class Chart:  # type: ignore
        pass

from .models import Order

class OrdersByDayChart(Chart):
    """Simple chart example counting orders per day.

    If admin_charts isn't installed the Chart base will be a no-op stub; the
    admin integration can be added later once the dependency is installed.
    """
    title = 'Orders by Day'
    template = 'admin_charts/charts/line_chart.html'

    def get_data(self):
        from django.db.models.functions import TruncDay
        from django.db.models import Count

        # Use the actual datetime field on Order (ordered_at) defined in models
        order_counts = (Order.objects
                        .annotate(day=TruncDay('ordered_at'))
                        .values('day')
                        .annotate(count=Count('id'))
                        .order_by('day'))

        return {
            'labels': [item['day'].strftime('%Y-%m-%d') for item in order_counts],
            'datasets': [{
                'label': 'Orders',
                'data': [item['count'] for item in order_counts],
            }]
        }