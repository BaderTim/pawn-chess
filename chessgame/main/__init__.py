



def main():
    print("\n---WELCOME TO BAUERNSCHACH---\n")
    update_display([])



def update_display(figures):
    """
    input is a array with all the figures on the field
    -generates 1d table array
    -fills array with figures
    -outputs array to console
    """
    table = []
    for counter in range(64): #generates table array --> 1D array to describe schachfeld
        table.append("_")

    for _, figure in enumerate(figures): #fills table array with figure positions
        table[(8-figure.pos_y)*8+figure.pos_x] = figure.color #figure positions are 2d, by multiplying them we can get the position in the 1d array

    table_output = "   A  B  C  D  E  F  G  H\n8  "
    line_space = 0
    coordinate_system_y = 8
    for _, pos in enumerate(table): #builds output string in form of a schachfeld
        table_output += f"{pos}  "
        line_space += 1
        if line_space == 8: #creates a line space after every 8 fields
            left_side_y = coordinate_system_y - 1
            if left_side_y > 0:
                table_output += f" {coordinate_system_y}\n{left_side_y}  "
            else:
                table_output += f" {coordinate_system_y}\n"
            coordinate_system_y -= 1
            line_space = 0
    table_output += "\n   A  B  C  D  E  F  G  H"
    print(table_output)





if __name__ == '__main__':
    main()