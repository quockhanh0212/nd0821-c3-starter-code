from starter.train_model import training
import hydra
from omegaconf import DictConfig


if __name__ == "__main__":
    import hydra
    from omegaconf import DictConfig, OmegaConf

    @hydra.main(config_path=".", config_name="config", version_base="1.2")
    def main(config: DictConfig) -> None:
        training(config)

    main()