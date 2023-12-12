# 1939
# 18e : le principe
# 1866, Robert Whitehead : correc de trajec de torpille
# 1868, James Clerk Maxwell : régul vitesse rotation
# 1922, Nicolas Minorsky : système de pilotage automatique de navire
# 1939, entreprises Taylor Instrument et Foxboro Instrument : 1ères implémentations de régulateurs PID mécaniques
# 1951, entreprise Swartwout : 1ers PID électroniques
# Algorithme PID (Proportional, Integral, Derivative)
# Auteur: Inconnu

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        # Paramètres du PID
        self.Kp = Kp  # Gain proportionnel
        self.Ki = Ki  # Gain intégral
        self.Kd = Kd  # Gain dérivatif

        # Variables pour le PID
        self.prev_error = 0.0  # Erreur précédente
        self.integral = 0.0    # Terme intégral

    def compute(self, setpoint, process_variable):
        # Calcul de l'erreur
        error = setpoint - process_variable

        # Calcul du terme proportionnel
        proportional = self.Kp * error

        # Calcul du terme intégral
        self.integral += error
        integral = self.Ki * self.integral

        # Calcul du terme dérivatif
        derivative = self.Kd * (error - self.prev_error)
        self.prev_error = error

        # Calcul de la sortie totale
        output = proportional + integral + derivative

        return output

# Exemple d'utilisation du PID
# pid = PIDController(Kp, Ki, Kd)
# output = pid.compute(setpoint, process_variable)