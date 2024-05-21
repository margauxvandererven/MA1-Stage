

def syntspec(pathtofile):
    file = open(pathtofile)
    wavelen = []
    flux = []
    for line in file:
        i = line.split()
        wavelen.append(float(i[0]))
        flux.append(float(i[1]))
    return {'wavelen' : wavelen, 'flux' : flux }


def redshift_wavelen(wavelen, v):
    redshift = []
    c = 299792458 #m/s
    for i in wavelen:
        z = v/c * i
        k = i - z
        redshift.append(k)
    return redshift   


def mediane_5(liste):
    # Trie la liste dans l'ordre décroissant
    liste_triee = sorted(liste, reverse=True)
    
    # Calcule le nombre d'éléments à extraire (5%)
    nb_elements_a_extraire = int(len(liste) * 0.05)
    
    # Extrait les 5% plus grands éléments
    plus_grands = liste_triee[:nb_elements_a_extraire]
    
    # Trie la liste
    liste_triee2 = sorted(plus_grands)
    
    # Calcule la longueur de la liste
    longueur = len(liste_triee2)
    
    # Si le nombre d'éléments est impair
    if longueur % 2 != 0:
        mediane_index = longueur // 2
        mediane = liste_triee2[mediane_index]
    else:
        # Si le nombre d'éléments est pair
        mediane_index_1 = longueur // 2 - 1
        mediane_index_2 = longueur // 2
        mediane = (liste_triee2[mediane_index_1] + liste_triee2[mediane_index_2]) / 2
    
    return mediane



def zoom_syntspec(path, filename, wavelength, taille):
    wavelenB = syntspec(path+filename)['wavelen']
    fluxB = syntspec(path+filename)['flux']
    h = []
    for j in wavelenB:
        if 0 < j-wavelength:
            h.append(j)
    centre_synt = wavelenB.index(min(h))
    length = int(taille/0.005)
    
    return {"synt_wavelen" : wavelenB[centre_synt-length:centre_synt+length], "synt_flux" : fluxB[centre_synt-length:centre_synt+length]}


def zoom_syntspec2(path, filename, z_wavelen, flux, wavelength):
    wavelenB = syntspec(path+filename)['wavelen']
    fluxB = syntspec(path+filename)['flux']
    k = []
    h = []
    for i in z_wavelen:
        if 0 < i-wavelength:
            k.append(i)
    centre = z_wavelen.index(min(k))

    for j in wavelenB:
        if 0 < j-wavelength:
            h.append(j)
    centre_synt = wavelenB.index(min(h))

    mediane = mediane_5(flux[centre-160:centre+160])

    flux_normalised = []
    for m in flux[centre-160:centre+160] :
        flux_normalised.append(m/mediane)

    return {"z_wavelen" : z_wavelen[centre-160:centre+160], "flux_normalised" : flux_normalised, 
            "synt_wavelen" : wavelenB[centre_synt-2000:centre_synt+2000], "synt_flux" : fluxB[centre_synt-2000:centre_synt+2000]}



def normalisation(z_wavelen, flux, wavelength):
    k = []
    h = []
    for i in z_wavelen:
        if 0 < i-wavelength:
            k.append(i)
    centre = z_wavelen.index(min(k))

    mediane = mediane_5(flux[centre-160:centre+160])

    flux_normalised = []
    for h in flux[centre-160:centre+160] :
        flux_normalised.append(h/mediane)
    return {"z_wavelen" : z_wavelen[centre-160:centre+160], "flux_normalised" : flux_normalised}


def normalisation2(z_wavelen, flux, wavelength, taille):
    k = []
    h = []
    for i in z_wavelen:
        if 0 < i-wavelength:
            k.append(i)
    centre = z_wavelen.index(min(k))
    mediane = mediane_5(flux[centre-taille:centre+taille])

    flux_normalised = []
    for h in flux[centre-160:centre+160] :
        flux_normalised.append(h/mediane)
    return {"z_wavelen" : z_wavelen[centre-taille:centre+taille], "flux_normalised" : flux_normalised}