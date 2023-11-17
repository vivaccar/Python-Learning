def ground_ship(weight, gtax):
    print("Ground Shipping Cost: $", weight * gtax + 20)

def drone_ship(weight, dtax):
    print("Drone Shipping Cost: $", weight * dtax)
    
def main():

    weight = float(input("What is the weight of your package? "))
    if weight <= 2:
        ground_ship(weight, 1.5)
        drone_ship(weight, 4.5)
    elif weight > 2 and weight <= 6:
        ground_ship(weight, 3)
        drone_ship(weight, 9)
    elif weight > 6 and weight <= 10:
        ground_ship(weight, 4)
        drone_ship(weight, 12)
    elif weight > 10:
        ground_ship(weight, 4.75)
        drone_ship(weight, 14.25)
    print("Flat Charge Cost: $ 125.00")
    
if __name__ == "__main__":
    main()