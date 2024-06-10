

from django.urls import path

from dos import views

urlpatterns = [
    path('', views.main, name='main'),
    path('log', views.log, name='log'),
    path('bank_home', views.bank_home, name='bank_home'),
    path('manage_branch', views.manage_branch, name='manage_branch'),
    path('manage_branch_search', views.manage_branch_search, name='manage_branch_search'),
    path('add_details', views.add_details, name='add_details'),
    path('edit_details/<int:id>', views.edit_details, name='edit_details'),
    path('delete_branch/<int:id>', views.delete_branch, name='delete_branch'),
    path('users', views.users, name='users'),
    path('reports', views.reports, name='reports'),
    path('reports_search', views.reports_search, name='reports_search'),
    path('complaints', views.complaints, name='complaints'),
    path('complaints_search', views.complaints_search, name='complaints_search'),
    path('replys/<int:id>', views.replys, name='replys'),
    path('reply_code', views.reply_code, name='reply_code'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('feedbacks_search', views.feedbacks_search, name='feedbacks_search'),
    path('edit_branch', views.edit_branch, name='edit_branch'),




    # ____________________________BRANCH____________________________________________________________


    path('accept_user', views.accept_user, name='accept_user'),
    path('accept_user_search', views.accept_user_search, name='accept_user_search'),
    path('branch_home', views.branch_home, name='branch_home'),
    path('allocate_account_details', views. allocate_account_details, name=' allocate_account_details'),
    path('allocation/<int:id>/<int:rid>', views.allocation, name='allocation'),
    path('allocation_post', views.allocation_post, name='allocation_post'),
    path('rejection/<int:rid>', views.rejection, name='rejection'),
    path('send_report', views.send_report, name='send_report'),
    path('report_post', views.report_post, name='report_post'),
    path('transaction_details', views.transaction_details, name='transaction_details'),
    path('transaction_details_search', views.transaction_details_search, name='transaction_details_search'),

    path('update', views.update, name='update'),
    path('view_feedback', views.view_feedback, name='view_feedback'),
    path('feedback', views.feedback, name='feedback'),
    path('view_feedback_search', views.view_feedback_search, name='view_feedback_search'),
    # ____________________________________USER_______________________________________________________

    path('registration', views.registration, name=' registration'),
    path('send_acrequest', views. send_acrequest, name='send_acrequest'),
    path('send_acc_req/<int:id>', views. send_acc_req, name='send_acc_req'),
    path('send_complaint', views.send_complaint, name='send_complaint'),
    path('send_complaint_post', views.send_complaint_post, name='send_complaint_post'),
    path('send_feedback', views.send_feedback, name='send_feedback'),
    path('send_feedback_post', views.send_feedback_post, name='send_feedback_post'),
    path('view_transaction', views.view_transaction, name='view_transaction'),
    path('view_transaction_search', views.view_transaction_search, name='view_transaction_search'),
    path('user_home', views.user_home, name='user_home'),
    path('send_request', views.send_request, name='send_request'),
    path('select_branch', views.select_branch, name='select_branch'),
    path('usersearch', views.usersearch, name='usersearch'),
    path('branch_code', views.branch_code, name='branch_code'),
    path('view_reply', views.view_reply, name='view_reply'),
    path('view_account_detais_new', views.view_account_detais_new, name='view_account_detais_new'),
    path('view_account_details_search', views.view_account_details_search, name='view_account_details_search'),
    path('add_update', views.add_update, name='add_update'),
    path('logout', views.logout, name='logout'),
    path('registration_s', views.registration_s, name='registration_s'),
    path('Register_post', views.Register_post, name=' Register_post'),
]
