from django.conf.urls import url, include
import analytics.views as analytics_views

urlpatterns = [

    url(r"^piechart/$", analytics_views.display_piechart, name="piechart"),
    url(r"^linechart/$", analytics_views.display_line_chart, name="linechart"),
    url(r"^barchart/$", analytics_views.display_bar_chart, name="display_bar_chart"),
    url(r"^order/(?P<status>[\w]+)/$", analytics_views.display_order_status, name="display_order_status"),
    url(r"^generatepdf/$", analytics_views.generate_pdf, name="generate_pdf"),
    
]