
def calculate_bmi(weight, height):
    """Oblicza BMI na podstawie wagi (kg) i wzrostu (m)."""
    BMI = weight / (height ** 2)
    return BMI

def classify_bmi(BMI):
    """Klasyfikuje BMI zgodnie z wytycznymi WHO."""
    if BMI < 18.5:
        return "Niedowaga"
    elif 18.5 <= BMI < 25:
        return "Waga prawidłowa"
    elif 25 <= BMI < 30:
        return "Nadwaga"
    else:
        return "Otyłość"
    
if __name__ == "__main__":
    weight = float(input("Podaj masę ciała (w kilogramach): "))
    height = float(input("Podaj wzrost (w metrach): "))
    
    BMI = calculate_bmi(weight, height)
    classification = classify_bmi(BMI)
    
    print(f"BMI = {BMI:.2f}")
    print(classification)