from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include, patterns
from home import views as home_views
from about import views as about_views
from contact import views as contact_views
from blog import views as blog_views
from portfolio import views as portfolio_views
from history import views as history_views
from mission import views as mission_views
from coorporate_governance import views as coorporate_governance_views
from management_board import views as management_board_views
from group_societies import views as group_societies_views
from social_responsibility import views as social_responsibility_views
from human_resources import views as human_resources_views
from students_practice import views as students_practice
from employment_opportunities import views as employment_opportunities
from gallery import views as gallery_views
from job import views as job_views
from elite import views as elite_views
from partners import views as parners_views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^crazyadmin/', include(admin.site.urls)),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]

urlpatterns += [
    url(r"^search/", elite_views.SearchViewCustom.as_view(), name='search_view_watson'),
]

urlpatterns += [
    url(r'^froala_editor/', include('froala_editor.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^$', RedirectView.as_view(url='home', permanent=False)),
]

urlpatterns += [
    url(r'^imagefit/', include('imagefit.urls')),
]

urlpatterns += [
    url(r'^home/$', home_views.Home.as_view(), name='home'),
]

urlpatterns += [
    url(r'^contact/$', contact_views.Contact.as_view(), name='contact'),
]

urlpatterns += [
    url(r'^about/$', about_views.About.as_view(), name='about'),
]

urlpatterns += [
    url(r'^blog/$', blog_views.Blog.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', blog_views.BlogDetail.as_view(), name='blog_detail'),
    url(r'^categories/blog/(?P<slug>[\w-]+)/$', blog_views.CategoryDetail.as_view(), name='category_detail_blog'),
    url(r'^tags/blog/(?P<slug>[\w-]+)/$', blog_views.TagDetail.as_view(), name='tag_detail_blog'),
]

urlpatterns += [
    url(r'^portfolio/$', portfolio_views.PortfolioList.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<slug>[\w-]+)/$', portfolio_views.PortfolioDetail.as_view(), name='portfolio_detail'),
    url(r'^categories/portfolio/(?P<slug>[\w-]+)/$', portfolio_views.CategoryDetail.as_view(), name='category_detail_portfolio'),
    url(r'^tags/portfolio/(?P<slug>[\w-]+)/$', portfolio_views.TagDetail.as_view(), name='tag_detail_portfolio'),
]

urlpatterns += [
    url(r'^history/$', history_views.History.as_view(), name='history'),
]

urlpatterns += [
    url(r'^mission/$', mission_views.Mission.as_view(), name='mission'),
]

urlpatterns += [
    url(r'^coorporate-governance/$', coorporate_governance_views.Coorporate.as_view(), name='coorporate'),
]

urlpatterns += [
    url(r'^management-board/$', management_board_views.Management.as_view(), name='management'),
    url(r'^management-board/(?P<slug>[\w-]+)/$', management_board_views.BoardMemberDetail.as_view(), name='board_member_detail'),
]

urlpatterns += [
    url(r'^group-socities/$', group_societies_views.GroupSocities.as_view(), name='group_socities'),
]

urlpatterns += [
    url(r'^social-responsibility/$', social_responsibility_views.SocialResponsibility.as_view(), name='social_responsibility'),
]

urlpatterns += [
    url(r'^human-resources/$', human_resources_views.HumanResources.as_view(), name='human_resources'),
]

urlpatterns += [
    url(r'^students-practice/$', students_practice.StudentsPractice.as_view(), name='students_practice'),
]

urlpatterns += [
    url(r'^employment-opportunities/$', employment_opportunities.EmploymentOpportunities.as_view(), name='employment_opportunities'),
    url(r'^jobs/(?P<slug>[\w-]+)/apply$', employment_opportunities.JobApply.as_view(), name='job_apply'),
    url(r'^jobs/(?P<slug>[\w-]+)/$', employment_opportunities.JobDetail.as_view(), name='job_detail'),
    url(r'^get-job-details/$', employment_opportunities.JobDetailAjax, name='job_detail_ajax'),
    url(r'^categories/jobs/(?P<slug>[\w-]+)/$', employment_opportunities.CategoryDetail.as_view(), name='category_detail_jobs'),
    url(r'^tags/jobs/(?P<slug>[\w-]+)/$', employment_opportunities.TagDetail.as_view(), name='tag_detail_jobs'),
]

urlpatterns += [
    url(r'^gallery/$', gallery_views.ImageGallery.as_view(), name='image_gallery'),
]

urlpatterns += [
    url(r'^partners/(?P<slug>[\w-]+)/$', parners_views.PartnerDetail.as_view(), name='partner_detail'),
]