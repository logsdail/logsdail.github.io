from chemsh import *

# Function used to print cluster stored in the fragment
def print_frag(frag):
    print()
    print(frag.coords2str())
    print("Number of atoms:", frag.natoms)
    print()

# Creation of mfi cluster fragment
mfi = Fragment(coords='mfi.pun', connmode='covalent')

# Displays mfi cluster before amendments
print("The structure of the silicate is:")
print_frag(mfi)

# Deletion and insertion of appropriate atoms to form zeolite cluster
mfi.names[0] = 'Al'
mfi.znums[0] = 13
mfi.insert('H', 550)
mfi.coords[550] = -1.65333239913411e+01, -6.10680708115438e+00, 8.97525903483508e+00
mfi.charges[550] = 0.00000

# Displays zsm5 cluster 
print("With the addition of Al and H, the structure of the zeolite is:")
print_frag(mfi)

# Saving of zsm5 cluster
mfi.save('zsm5_new.pun', 'pun')
