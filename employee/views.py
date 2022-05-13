from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Department, Group, EmployeeInfo, Employee

"""
Department
"""


def list_dep_old(request):
    dep_list = Department.objects.all()
    return render(request, 'department/list_dep_old.html', {'dep_list': dep_list})


def add_dep_old(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'department/add_dep_old.html', {'error_info': '部门名称不能为空！'})
        try:
            # 用create()函数新建一条记录，这条记录会自动保存，不用调用save()函数
            p = Department.objects.create(dep_name=dep_name, dep_script=dep_script)
            # 这里还可以使用如下方式来新建新建一条记录。
            # dic = {"dep_name": dep_name, "dep_script": dep_script}
            # Department.create(**dic)
            # 生成新的记录后，通过redirect重定向到部门列表页面，参数匹配的是URL配置项
            return redirect('/test_orm_old/list_dep_old')
        except Exception as e:
            return render(request, 'department/add_dep_old.html', {'error_info': '输入部门名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'department/add_dep_old.html')


def del_dep_old(request, dep_id):
    # 通过get()函数取得一条记录
    dep_object = Department.objects.get(id=dep_id)
    # 删除部门记录
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old')


def edit_dep_old(request, dep_id):
    # 判断请求方式
    if request.method == 'POST':
        id = request.POST.get('id')
        # 获取前端页面提交的数据
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = Department.objects.get(id=id)
        # 给字段赋值
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        # 保存数据到数据库表
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object = Department.objects.get(id=dep_id)
        return render(request, 'department/edit_dep_old.html', {'department': dep_object})


"""
Group
"""


def list_group_old(request):
    group_list = Group.objects.all()
    return render(request, 'group/list_group_old.html', {'group_list': group_list})


def add_group_old(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        # 团体名称group_name为空时，向网页传递错误信息
        if group_name.strip() == '':
            return render(request, 'group/add_group_old.html', {'error_info': '团体名称不能为空！'})
        try:
            Group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/test_orm_old/list_group_old')
        except Exception as e:
            return render(request, 'group/add_group_old.html', {'error_info': '输入团体名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'group/add_group_old.html')


def del_group_old(request, group_id):
    group_object = Group.objects.get(id=group_id)
    group_object.delete()
    return redirect('/test_orm_old/list_group_old/')


def edit_group_old(request, group_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        group_object = Group.objects.get(id=id)
        group_object.group_name = group_name
        group_object.group_script = group_script
        group_object.save()
        return redirect('/test_orm_old/list_group_old/')
    else:
        group_object = Group.objects.get(id=group_id)
        return render(request, 'group/edit_group_old.html', {'group': group_object})


"""
EmployeeInfo
"""


def list_employeeinfo_old(request):
    info_list = EmployeeInfo.objects.all()
    return render(request, 'employeeinfo/list_employeeinfo_old.html', {'info_list': info_list})


def add_employeeinfo_old(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip() == '':
            return render(request, 'employeeinfo/add_employeeinfo_old.html', {'error_info': '电话号码不能为空！'})
        try:
            EmployeeInfo.objects.create(phone=phone, address=address)
            return redirect('/test_orm_old/list_employeeinfo_old/')
        except Exception as e:
            return render(request, 'employeeinfo/add_employeeinfo_old.html', {'error_info': '信息有错误！'})
        finally:
            pass
    return render(request, 'employeeinfo/add_employeeinfo_old.html')


def del_employeeinfo_old(request, info_id):
    info_object = EmployeeInfo.objects.get(id=info_id)
    info_object.delete()
    return redirect('/test_orm_old/list_employeeinfo_old/')


def edit_employeeinfo_old(request, info_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info_object = EmployeeInfo.objects.get(id=id)
        info_object.phone = phone
        info_object.address = address
        info_object.save()
        return redirect('/test_orm_old/list_employeeinfo_old/')
    else:
        info_object = EmployeeInfo.objects.get(id=info_id)
        return render(request, 'employeeinfo/edit_employeeinfo_old.html', {'info': info_object})


"""
Employee
"""


def list_employee_old(request):
    # 取出employee数据表中全部记录
    emp = Employee.objects.all()
    return render(request, 'employee/list_employee_old.html', {'emp_list': emp})


def del_employee_old(request, emp_id):
    # 取出主键值等于emp_id的记录对象
    emp = Employee.objects.get(id=emp_id)
    # 删除记录对象
    emp.delete()
    return redirect('/test_orm_old/list_employee_old')


def add_employee_old(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")
        info = request.POST.get("info")
        salary = request.POST.get("salary")
        # 取得多个值
        groups = request.POST.getlist("group")
        new_emp = Employee.objects.create(name=name, email=email, salary=salary, dep_id=dep, info_id=info)
        # 给多对多键字段赋值
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')
    dep_list = Department.objects.all()
    group_list = Group.objects.all()
    info_list = EmployeeInfo.objects.all()
    return render(request, 'employee/add_employee_old.html',
                  {'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


def edit_employee_old(request, emp_id):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")
        info = request.POST.get("info")
        groups = request.POST.getlist("group")

        emp = Employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.dep_id = dep
        emp.info_id = info
        emp.group.set(groups)
        emp.save()
        return redirect('/test_orm_old/list_employee_old/')
    emp = Employee.objects.get(id=emp_id)
    dep_list = Department.objects.all()
    group_list = Group.objects.all()
    info_list = EmployeeInfo.objects.all()
    return render(request, 'employee/edit_employee_old.html',
                  {'emp': emp, 'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


def test_foreign(request):
    # 正向操作，通过外键值dep关联到department数据表的一条记录，然后取得该记录的dep_name字段
    emp = Employee.objects.get(id=7)
    dep_name = emp.dep.dep_name

    # 反向操作，通过employee_set关联到employee数据表，然后用all()函数
    dep_obj = Department.objects.get(id=18)
    emp_list = dep_obj.employee_set.all()
    emp_names = [emp.name for emp in emp_list]
    return HttpResponse("1.正向关联：员工名称：{0},所在部门名称:{1}<br> "
                        "2.反向查找：部门名称:{2},部门员工:{3}".format(emp.name, dep_name, dep_obj.dep_name, emp_names))
