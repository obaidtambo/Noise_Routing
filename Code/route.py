# @ author Obaid Tamboli


import librosa
import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from numpy import exp
from PIL import Image as im


# Load the audio file
audio_file = ".\ZOOM0001_comp.wav"
audio_data, sr = librosa.load(audio_file)

fig, ax = plt.subplots(nrows=1, sharex=True)
librosa.display.waveshow(audio_data, sr=sr,)
ax.set(title='Amplitude Values')
ax.label_outer()
plt.show()
amplitude_values = np.abs(librosa.stft(audio_data)).mean(axis=0)

#  to change the audio u can play with the miultiples of 10201 within the data range
amplitude_values=amplitude_values[0*10201: 1*10201]
amplitude_values_norm=np.interp(amplitude_values, (amplitude_values.min(), amplitude_values.max()), (0, +255))
amplitude_values_norm = amplitude_values_norm.reshape(101, 101)


data = im.fromarray(amplitude_values_norm)
data.show()


def simulated_annealing(start=(0,0), end=(10,10), n_iterations=100, step_size= 0.1, temp=10):
    # generate a way-points list
    best_waypoints = [(random.uniform(1, 9), random.uniform(1, 9)) for i in range (8)]
    best_route = [start] + sorted(best_waypoints) + [end]
    # evaluate the initial route
    best_eval = fitness(best_route)

    # current working solution
    curr_waypoints, curr_eval = best_waypoints, best_eval
    scores = list()

    for i in range(n_iterations):
        candidate_waypoints= [ ( min(i[0] + (random.uniform(1, 9) * step_size), 10.0) ,min(i[1] + (random.uniform(1, 9) * step_size) ,10.0))  for i in curr_waypoints]
        candidate_route = [start] +  sorted(candidate_waypoints) + [end] #candidate_waypoints.sort() 


        # evaluate candidate point
        candidate_eval = fitness(candidate_route)
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best_waypoints, best_eval = candidate_waypoints, candidate_eval
            best_route = candidate_route

			# keep track of scores
            scores.append(best_eval)
			# report progress
            print('  >%d f(%s) = %.5f' % (i, best_route, best_eval))

        # difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # calculate temperature for current epoch
        t = temp / float(i + 1)
		# calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
		# check if we should keep the new point
        if diff < 0 or random.random() < metropolis:
			# store the new current point
            curr_waypoints, curr_eval = candidate_waypoints, candidate_eval

    return [best_route, best_eval, scores]



# hill climbing local search algorithm
def hillclimbing(start=(0,0), end=(10,10), n_iterations=100, step_size=0.1):
    # generate an initial way-points solution
    best_waypoints = [(random.uniform(1, 9), random.uniform(1, 9)) for i in range (8)]
    best_route = [start] + sorted(best_waypoints) + [end]

    # evaluate the initial route
    best_eval = fitness(best_route)
    # run the hill climb
    scores = list()
    scores.append(best_eval)
    for i in range(n_iterations):
        # take a step
        candidate_waypoints= [ ( min(i[0] + (random.uniform(1, 9) * step_size), 10.0) ,min(i[1] + (random.uniform(1, 9) * step_size) ,10.0))  for i in best_waypoints]
        candidate_route = [start] +  sorted(candidate_waypoints) + [end] 
		# take a step
		
		# evaluate candidate point
        candidte_eval = fitness(candidate_route)
		# check if we should keep the new point
        if candidte_eval <= best_eval:
            # store the new point
            best_route, best_eval = candidate_route, candidte_eval
            best_waypoints=candidate_waypoints

            # keep track of scores
            scores.append(best_eval)
            # report progress
            print('>%d f(%s) = %.5f' % (i, best_route, best_eval))

    return [best_route, best_eval, scores]


def fitness(route,amplitude_values_norm=amplitude_values_norm):
    distance = 0
    noise=0
    for i in range(len(route)-1):
        x1, y1 = route[i]
        x2, y2 = route[i+1]
        n1=amplitude_values_norm[int(x1*10)-1][int(y1*10)-1]
        n2=amplitude_values_norm[int(x2*10)-1][int(y2*10)-1]
        distance += ((x2-x1)**2 + (y2-y1)**2)**0.5
        noise += (((n1)**2 + (n2)**2)**0.5)
        # noise+= n1-n2
        # distance += (abs(x1-x1) + abs(y2-y1))
    return noise*distance


def dist(route):
    distance = 0
    for i in range(len(route)-1):
        x1, y1 = route[i]
        x2, y2 = route[i+1]
        distance += ((x2-x1)**2 + (y2-y1)**2)**0.5
        # distance += (abs(x1-x1) + abs(y2-y1))
    return distance

def noise(route,amplitude_values_norm=amplitude_values_norm):
    noise = 0
    for i in range(len(route)-1):
        x1, y1 = route[i]
        x2, y2 = route[i+1]
        n1=amplitude_values_norm[int(x1*10)-1][int(y1*10)-1]
        n2=amplitude_values_norm[int(x2*10)-1][int(y2*10)-1]
        noise += (((n1)**2 + (n2)**2)**0.5)/2

        # distance += (abs(x1-x1) + abs(y2-y1))
    return noise     




