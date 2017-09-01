from django import template

register = template.Library()

@register.filter(name = 'in_list')
def in_list(value,arg):
	for a in arg:
		if value == a.user:
			return True
	return False
