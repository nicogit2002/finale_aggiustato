import os


# Funzione creazione sala

def crea_sala():
    ''' Crea la lista di liste per rappresentare la sala cinematografica
    '''
    sala = []
    for i in range(5):
        if i == 3:                    
            fila = ['V'] * 10         
        else:
            fila = ['L'] * 10        
        sala.append(fila)
    return sala

 
# Visualizzazione della sala
 
def mostra_sala(sala):
    ''' Mostra su terminale l'attuale disposizione della sala

    @sala lista di liste contenente lo stato occupazionale della sala
    '''
    print("\n========= SALA CINEMA PARADISO ========")
    print("      ", end="")
    
    for posto in range(1, 11):                        
        print(f"{posto:2}", end=" ")
    print()
    
    for i, fila in enumerate(sala, start=1):          
        print(f"Fila {i}: ", end="")                  
        for posto in fila:                           
            print(f"{posto:2}", end=" ")
        print()
    print("==========================================")
    print("L = libero  V = VIP libero  X = occupato")
 
 
 
# Prenotazione di un posto
 
def prenota(sala, fila, posto):
    ''' Funzione che gestisce la prenotazione di un posto

    @sala lista di liste contenente l'attuale stato della sala

    @fila int, variabile contenente la fila che si vuole prenotare 

    @posto int, variabile contenente il posto, all'interno della fila, che si vuole prenotare
    '''
   
    if fila < 1 or fila > 5 or posto < 1 or posto > 10:      
        return None                                         
    
    # Conversione delle coordinate in indici Python
    fila = fila - 1
    posto = posto - 1
    
    # Controllo della disponibilità
    if sala[fila][posto] == "X":       
        return False                   
 
    if sala[fila][posto] == "V":
        risposta = input(f"Hai selezionato un posto VIP ( Fila {fila}, Posto{posto}). Sei sicuro? (s/n): ").strip().lower()
        
        if risposta == 's':
            sala[fila][posto] = "X"
            return "VIP"
        else:
            print("Prenotazione VIP annullata.")
            return False
 
    sala[fila][posto] = "X"            
    return True
