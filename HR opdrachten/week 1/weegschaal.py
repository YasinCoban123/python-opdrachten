widget_weight = 75  
gizmo_weight = 112 


num_widgets = int(input("Hoeveelheid widgets: "))
num_gizmos = int(input("Hoeveelheid gizmos: "))


total_weight = (num_widgets * widget_weight) + (num_gizmos * gizmo_weight)


print(f"De totale gewicht van 1de bestelling is  {total_weight} gram")
