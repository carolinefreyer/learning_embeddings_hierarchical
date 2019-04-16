from network.ethec_experiments import ETHEC_train_model
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help='Use DEBUG mode.', action='store_true')
    parser.add_argument("--lr", help='Input learning rate.', type=float, default=0.01)
    parser.add_argument("--batch_size", help='Batch size.', type=int, default=8)
    parser.add_argument("--evaluator", help='Evaluator type.', type=str, default='ML')
    parser.add_argument("--experiment_name", help='Experiment name.', type=str, required=True)
    parser.add_argument("--experiment_dir", help='Experiment directory.', type=str, required=True)
    parser.add_argument("--image_dir", help='Image parent directory.', type=str, required=True)
    parser.add_argument("--n_epochs", help='Number of epochs to run training for.', type=int, required=True)
    parser.add_argument("--n_workers", help='Number of workers.', type=int, default=4)
    parser.add_argument("--eval_interval", help='Evaluate model every N intervals.', type=int, default=1)
    parser.add_argument("--resume", help='Continue training from last checkpoint.', action='store_true')
    parser.add_argument("--merged", help='Use dataset which has genus and species combined.', action='store_true')
    parser.add_argument("--model", help='NN model to use. Use one of [`multi_label`, `multi_level`]',
                        type=str, required=True)
    parser.add_argument("--loss", help='Loss function to use.', type=str, required=True)
    parser.add_argument("--freeze_weights", help='This flag fine tunes only the last layer.', action='store_true')
    parser.add_argument("--set_mode", help='If use training or testing mode (loads best model).', type=str,
                        required=True)
    args = parser.parse_args(['--n_epochs', '7', '--experiment_name', 'ethec_alexnet_remove', '--experiment_dir',
                              '../exp/ethec/multi_level', '--model', 'alexnet', '--set_mode', 'train', '--debug',
                              '--image_dir', '/media/ankit/DataPartition/IMAGO_build_test_resized', '--loss',
                              'multi_level', '--eval_interval', '1', '--merged', '--lr', '0.01', '--freeze_weights',
                              '--resume'])

    ETHEC_train_model(args)
