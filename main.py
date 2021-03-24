from data_parsers.yahoo import get_historical_data
from models.Simple import Simple
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = get_historical_data("intc")
    data["Date"] = data.index
    # plt.plot(data["Date"], data["Open"])
    # plt.show()

    model = Simple(data)
    results = model.learn(70)

    print(results)
    plt.plot(range(len(results)), results)
    plt.show()

    plt.plot(range(len(results)), [x[1] for x in results])
    plt.show()
