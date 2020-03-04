from django import template
from ..models import Menu

register = template.Library()


@register.simple_tag(name='show_menu_parent')
def show_menu_parent(username):
    '''
    获取用户权限
    '''
    if username == 'all':
        parent_menu_list = Menu.objects.filter(menu_level=1).all()
    else:
        parent_menu_list = Menu.objects.all()
    return parent_menu_list


@register.simple_tag(name='show_menu_son')
def show_menu_son(username, parent_id):
    '''
    获取用户权限
    '''
    if username == 'all':
        son_menu_list = Menu.objects.filter(parent_id=parent_id, menu_level=2).all()
    else:
        son_menu_list = Menu.objects.filter(parent_id=parent_id, menu_level=2).all()
    return son_menu_list
