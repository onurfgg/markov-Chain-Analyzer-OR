import numpy as np

class MarkovChainSimulator:
    def __init__(self, transition_matrix, states):
        """
        Markov Zinciri Simülatörü başlatılır.
        transition_matrix: 2D liste veya numpy array (Geçiş Matrisi)
        states: Durumların isimlerini içeren liste
        """
        self.P = np.array(transition_matrix)
        self.states = states
        self.n_states = len(states)
        
        # Olasılık matrisinin geçerliliğini kontrol et (Satır toplamları 1 olmalı)
        assert np.allclose(self.P.sum(axis=1), 1), "Hata: Geçiş matrisinde satır toplamları 1 olmalıdır!"
        
    def get_steady_state(self):
        """
        Uzun dönem (steady-state) olasılıklarını lineer denklem sistemi çözerek bulur.
        """
        # (P^T - I) * pi = 0 ve sum(pi) = 1
        A = np.append(self.P.T - np.eye(self.n_states), np.ones((1, self.n_states)), axis=0)
        b = np.zeros(self.n_states + 1)
        b[-1] = 1.0
        
        # En küçük kareler (least squares) yöntemi ile çöz
        pi = np.linalg.lstsq(A, b, rcond=None)[0]
        return np.round(pi, 4)

    def simulate_steps(self, initial_state_idx, steps):
        """
        Belirli bir adımdaki durum olasılıklarını hesaplar.
        """
        current_state = np.zeros(self.n_states)
        current_state[initial_state_idx] = 1.0
        
        print(f"Başlangıç Durumu: {self.states[initial_state_idx]}")
        for step in range(1, steps + 1):
            current_state = np.dot(current_state, self.P)
            print(f"Adım {step}: {np.round(current_state, 4)}")
            
        return np.round(current_state, 4)

# --- ÖRNEK KULLANIM ---
if __name__ == "__main__":
    # Örnek: Bir makinenin "Çalışıyor", "Arızalı", "Bakımda" durumları
    durumlar = ["Çalışıyor", "Arızalı", "Bakımda"]
    gecis_matrisi = [
        [0.7, 0.2, 0.1],
        [0.0, 0.5, 0.5],
        [0.4, 0.0, 0.6]
    ]

    simulator = MarkovChainSimulator(gecis_matrisi, durumlar)
    
    print("--- Uzun Dönem (Steady-State) Olasılıkları ---")
    uzun_donem = simulator.get_steady_state()
    for durum, olasilik in zip(durumlar, uzun_donem):
        print(f"{durum}: {olasilik}")
        
    print("\n--- 5 Adımlık Simülasyon (0. İndeksten Başlayarak) ---")
    simulator.simulate_steps(initial_state_idx=0, steps=5)
