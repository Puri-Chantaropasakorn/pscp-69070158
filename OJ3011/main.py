"""Colors"""

color1 = input()
color2 = input()

match color1 :
    case "Red" :
        match color2 :
            case "Red" :
                print("Red")
            case "Yellow" :
                print("Orange")
            case "Blue" :
                print("Violet")
            case _ :
                print("Error")
    case "Yellow" :
        match color2 :
            case "Red" :
                print("Orange")
            case "Yellow" :
                print("Yellow")
            case "Blue" :
                print("Green")
            case _ :
                print("Error")
    case "Blue" :
        match color2 :
            case "Red" :
                print("Violet")
            case "Yellow" :
                print("Green")
            case "Blue" :
                print("Blue")
            case _ :
                print("Error")
    case _ :
        print("Error")
