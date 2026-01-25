import tkinter as tk
import random


# -------------------------------
# Size of Ticket
# -------------------------------
row = 3
col = 9


# Column wise ranges
ranges = [
    (1, 9), (10, 19), (20, 29),
    (30, 39), (40, 49), (50, 59),
    (60, 69), (70, 79), (80, 90)
]


# -------------------------------
# Create 0-1 Matrix
# -------------------------------
def make_binary_matrix():

    while True:

        # Make empty matrix
        mat = []

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(0)
            mat.append(temp)

        # Put 5 ones in each row
        for i in range(row):

            count = 0

            while count < 5:

                j = random.randint(0, 8)

                if mat[i][j] == 0:
                    mat[i][j] = 1
                    count = count + 1


        # Check each column has at least one 1
        ok = True

        for j in range(col):

            s = 0

            for i in range(row):
                s = s + mat[i][j]

            if s == 0:
                ok = False
                break


        if ok == True:
            return mat


# -------------------------------
# Fill Numbers
# -------------------------------
def fill_ticket(binary):

    ticket = []

    # Create empty ticket
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(0)
        ticket.append(temp)


    # Fill column wise
    for j in range(col):

        cnt = 0

        # Count how many 1 in column
        for i in range(row):
            if binary[i][j] == 1:
                cnt = cnt + 1


        low = ranges[j][0]
        high = ranges[j][1]


        # Generate random numbers
        nums = random.sample(range(low, high+1), cnt)
        nums.sort()


        k = 0

        for i in range(row):

            if binary[i][j] == 1:

                ticket[i][j] = nums[k]
                k = k + 1


    return ticket


# -------------------------------
# Generate Ticket
# -------------------------------
def generate():

    binary = make_binary_matrix()

    ticket = fill_ticket(binary)

    show(ticket)


# -------------------------------
# Display Ticket
# -------------------------------
def show(ticket):

    for w in box.winfo_children():
        w.destroy()


    for i in range(row):

        for j in range(col):

            if ticket[i][j] == 0:
                t = ""
            else:
                t = str(ticket[i][j])


            lab = tk.Label(
                box,
                text=t,
                width=5,
                height=2,
                font=("Arial", 14),
                border=2,
                relief="solid"
            )

            lab.grid(row=i, column=j, padx=2, pady=2)


# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("Tambola Ticket")


btn = tk.Button(
    root,
    text="Generate",
    font=("Arial", 14),
    command=generate
)

btn.pack(pady=10)


box = tk.Frame(root)
box.pack()


root.mainloop()
