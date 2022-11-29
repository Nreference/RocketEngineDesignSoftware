g = 9.80665


def idealThrustEquation(thrustCoefficient, nozzleStagnationPressure, throatArea):
    return thrustCoefficient * nozzleStagnationPressure * throatArea


def actualThrustEquation(thrustCoefficientEfficiency, thrustCoefficient, nozzleStagnationPressure, throatArea,
                         localAtmosphericPressure, exitArea):
    return (thrustCoefficientEfficiency * thrustCoefficient * nozzleStagnationPressure * throatArea
            - localAtmosphericPressure * exitArea)


def specificImpulse(thrust, massFlowRate, metric):
    if metric == 1:
        return thrust / (massFlowRate * g)
    elif metric == 0:
        return thrust / massFlowRate
    else:
        raise Exception("Metric argument must be set to on(1) or off(0)")
