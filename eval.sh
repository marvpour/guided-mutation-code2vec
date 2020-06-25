# echo "orig -> 5t"
# python code2vec.py --load models/models/orig/models/orig_iter10 --test data/orig2/orig2.test.c2v
#
#
# echo "orig -> orig"
# python code2vec.py --load models/models/orig/models/orig_iter10 --test data/orig/orig.test.c2v
#
echo "5t -> orig"
python code2vec.py --load models/models/hundred_epoch_mutated/models/hundred_epoch_mutated_iter99 --test data/orig/orig.test.c2v

echo "5t -> 5t"
python code2vec.py --load models/models/hundred_epoch_mutated/models/hundred_epoch_mutated_iter99 --test data/orig2/orig2.test.c2v
