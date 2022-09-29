import math

def main():

    max_cost_efficiency = -1 
    best_cost = None
##############################################################  Functions ##########################################################################


        #Function to computes the volume of the can sizes.
    def compute_volume(radius,height):

        #volume = π radius2 height
        volume = math.pi * (radius **2) * height
        return volume

        #Function to computes the surface area of the can sizes.
    def compute_surface_area(radius,height):

        #surface_area = 2π radius (radius + height)
        surface_area = (2 * math.pi) * radius * (radius + height)
        return surface_area

        #Function to computes the storage efficiency of the can sizes.
    def compute_storage_efficiency(volume, suface_area):

        #storage_efficiency = volume / surface_area
        volume = compute_volume(radius,height)
        suface_area = compute_surface_area(radius,height )
        storage_efficiency = volume / suface_area
        return storage_efficiency
        
    def compute_cost_efficiency(radius, height, cost):

        #cost_efficiency = volume / cost
        volume = compute_volume(radius,height)
        cost_efficiency = volume / cost
        return cost_efficiency

    
##############################################################  Objects ##########################################################################
    
    print('') #Space

    can_sizes = [

        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]

    ]

    for i in range(len(can_sizes)):
        #Get all elements in space 0 in list
        name = can_sizes[i][0]
        #Get all elements in space 1 in list
        radius = can_sizes[i][1]
        #Get all elements in space 2 in list
        height = can_sizes[i][2]
        #Get all elements in space 3 in list
        cost = can_sizes[i][3]
        
        #Object
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        print(f'Item: {name} - Storage efficiency: {storage_efficiency:.2f} - Cost efficience: {cost_efficiency:.2f}')
        
        #Acumulator to know which is the most cost_efficiency item
        if max_cost_efficiency < cost_efficiency :
            best_cost = name
            max_cost_efficiency = cost_efficiency

    print('') #Space
    print(f'Max cost efficiency {max_cost_efficiency:.2f}')
    print(f'Item more efficiency: {best_cost}')
    print('') #Space
    
main()