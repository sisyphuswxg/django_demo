from django.urls import path, include
from . import views


app_name = 'employee'

urlpatterns = [
    # 操作员工数据表 相关URL配置项 - ok
    path('list_employee_old/', views.list_employee_old),
    path('add_employee_old/', views.add_employee_old),
    path('edit_employee_old/<int:emp_id>/', views.edit_employee_old),
    path('del_employee_old/<int:emp_id>/', views.del_employee_old),

    # 操作部门数据表 相关URL配置项 - ok
    path('list_dep_old/', views.list_dep_old),
    path('add_dep_old/', views.add_dep_old),
    path('edit_dep_old/<int:dep_id>/', views.edit_dep_old),
    path('del_dep_old/<int:dep_id>/', views.del_dep_old),

    # 操作团体数据表 相关URL配置项 - ok
    path('list_group_old/', views.list_group_old),
    path('add_group_old/', views.add_group_old),
    path('edit_group_old/<int:group_id>/', views.edit_group_old),
    path('del_group_old/<int:group_id>/', views.del_group_old),

    # 操作员工补充信息数据表 相关URL配置项 - ok
    path('list_employeeinfo_old/', views.list_employeeinfo_old),
    path('add_employeeinfo_old/', views.add_employeeinfo_old),
    path('edit_employeeinfo_old/<int:info_id>/', views.edit_employeeinfo_old),
    path('del_employeeinfo_old/<int:info_id>/', views.del_employeeinfo_old),

    # 外键跨表操作demo
    path('test_foreign/', views.test_foreign),

]