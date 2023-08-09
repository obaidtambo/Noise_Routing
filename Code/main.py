# @ author Obaid Tamboli



from matplotlib import pyplot
import route 


# taking user input for tuple elements

print("****** INSTRUCTIONS ********")
print(" we have formulated this problem as an Point optimization problem , we take in a \n Start point and an End-point between (0,0) and (10,10) \n along with Number of iterations, stepsize and temp if the user wants to specifiy those")
start=(0,0)
end=(10,10)
try:
    print( " enter the Starting tuple as x and y co-ordinates")
    x = input("Enter the x element of the tuple: ")
    y = input("Enter the y element of the tuple: ")
    start= (float(x), float(y))
    print( " enter the Ending tuple as x and y co-ordinates")
    x = input("Enter the x element of the tuple: ")
    y = input("Enter the y element of the tuple: ")
    end=(float(x), float(y))
    print (" your CHOICEs \n Stimulated Annealing : 1 \n Enforced Hill Cilimbing : 2 ")
    choice= input(" your choice: ")
    if int(choice)== 2:
        print(" we recommend you continue with defaults")
        try:
            check= input(" Y/N: ")
            if check== 'N' or check=='n':
            
                n_iterations=input(" Enter a Max Iterations: ")
                step_size= input(" Enter a Step Size: ")
                # temp=input(" Enter a temp: ")
                # perform the hill climbing search
                best, score, scores =route.hillclimbing(start, end, n_iterations, step_size)
            else:    # perform the hill climbing search
                best, score, scores =route.hillclimbing(start, end, n_iterations=100, step_size=0.1)
        except ValueError:
            print(" using Deafults Because some Input error")
            best, score, scores =route.hillclimbing(start, end, n_iterations=100, step_size=0.1)
            
    else :
        print(" we recommend you continue with defaults")
        try:
            check= input(" Y/N: ")
            if check== 'N' or check=='n':
            
                n_iterations=input(" Enter a Max Iterations: ")
                step_size= input(" Enter a Step Size: ")
                temp=input(" Enter a temp: ")
                best, score, scores = route.simulated_annealing(start, end, n_iterations, step_size, temp)
            else:
                best, score, scores = route.simulated_annealing(start, end, n_iterations=100, step_size=0.1, temp=10)
        except ValueError:
            print(" using Deafults Because some Input error")
            best, score, scores = route.simulated_annealing(start, end, n_iterations=100, step_size=0.1, temp=10)
            


except:
    print(" using Deafults with Stimulated Annealing Because some Input error")
    start=(0,0)
    end=(10,10)
    best, score, scores = route.simulated_annealing(start=(0,0), end=(10,10), n_iterations=100, step_size=0.1, temp=10)

print('*****************  Done! ******************')
print('f(%s) = %f' % (best, score))
# line plot of best scores
pyplot.plot(scores, '.-')
pyplot.xlabel('Improvement Number')
pyplot.ylabel(" Noise x Distance")
pyplot.show()
print("Distance travelled : ", route.dist(best))
print("Noise Encountered  : ", route.noise(best))
print("Eucledian Diatance : ", route.dist([start,end]) )
pyplot.plot([i[0] for i in best ], [i[1] for i in best ],  marker = 'o')
pyplot.title(" Path Generated ")
pyplot.show()
    


