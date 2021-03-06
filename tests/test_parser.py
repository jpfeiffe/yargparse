import yargparse
import unittest

class TestYArgumentParser(unittest.TestCase):
    def test_multiple_configs(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args('-c config.yaml config2.yaml'.split(' '))
        self.assertEqual(len(args.class_weights), 1)

    def test_base_config(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args()
        self.assertEqual(args.config, ['config.yaml'])
        self.assertEqual(args.train_param.deltas, [1, 2, 3])
        self.assertEqual(args.train_param.lr, [.1, .2, .3])
        self.assertEqual(args.features[0].dim, 100)
        self.assertEqual(args.features[0].type, "sparse")
        self.assertEqual(args.features[1].dim, 200)
        self.assertEqual(args.features[1].type, "dense")

    def test_update_vals(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args(['--train_param.deltas=[.5, .6, 7]'])
        self.assertEqual(args.config, ['config.yaml'])
        self.assertEqual(args.train_param.deltas, [.5, .6, 7])

    def test_splittypes(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args(['--train_param.deltas=[.5, .6, 7]'])
        self.assertEqual(args.train_param.deltas, [.5, .6, 7])

        parser = yargparse.YArgumentParser()
        args = parser.parse_args(['--train_param.deltas [.5, .6, 7]'])
        self.assertEqual(args.train_param.deltas, [.5, .6, 7])

        parser = yargparse.YArgumentParser()
        args = parser.parse_args(['--train_param.deltas:[.5, .6, 7]'])
        self.assertEqual(args.train_param.deltas, [.5, .6, 7])
    
    def test_list_assign(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args(['--matrix[1][0] 18'])
        self.assertEqual(args.matrix[1][0], 18)

    def test_nonevals(self):
        parser = yargparse.YArgumentParser()
        parser.add_argument('--train_epochs', default=None)
        args = parser.parse_args(['--matrix[1][0] 18'])
        self.assertEqual(args.train_epochs, 10)

    def test_lists(self):
        parser = yargparse.YArgumentParser()
        args = parser.parse_args()
        self.assertEqual(len(args.class_weights), 1)



if __name__ == '__main__':
    unittest.main()
