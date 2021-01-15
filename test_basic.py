from geogeometry import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# plot number of intersections as a function of lines drawn
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NUM = 50 # total number of lines drawn
intersections_global = []
for k in range(2,NUM+1):
    intersections_local = []
    for q in range(100):
        num_xs, _, lines = count_intersections(k)
        intersections_local.append(num_xs)
    intersections_global.append(intersections_local)

plt.figure(figsize=(16,12))
fig = plt.boxplot(intersections_global)
plt.rcParams.update({'font.size': 28})
plt.rc('font', family='serif')
plt.title('Number of Intersections vs Lines Drawn')
plt.xlabel('Number of Lines Drawn')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.savefig('intersections_counted.png')
plt.show()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# calculate average number of edges for mosaic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
max_lines = 20
global_mosaics_pass, global_mosaics_size = count_mosaics(max_lines)
plt.figure(figsize=(20,10))
for item in global_mosaics_size[0][0]:
    plt.boxplot(global_mosaics_size[0])
plt.show()

print("Mean: ", np.mean(global_mosaics_size[0]))
print("Max: ", np.max(global_mosaics_size[0]))
print("Mode: ", stats.mode(global_mosaics_size[0])[0][0])
print("Median: ", np.median(global_mosaics_size[0]))