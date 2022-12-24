# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# STYLE
# ///////////////////////////////////////////////////////////////
style ='''
QTabWidget {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QTabWidget:hover {{
	background-color: {_bg_color_hover};
}}
QTabWidget:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''