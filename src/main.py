from engine.train import train
from engine.generate import generate


def main():
    experiment_name = "2xgrvgac"
    experiment_name = train()
    generate(experiment_name)


if __name__ == "__main__":
    main()
