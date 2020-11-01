#!/bin/bash
#SBATCH --job-name=german
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --mem=10000M
#SBATCH -p gpu_shared

module load 2019
module load Python/3.7.5-foss-2019b


for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
do
    for data_type in train val test
    do
        python translate.py -model "models/lstms2s_${i}.pt" -src "../unimorph/${data_type}.src" \
                            -gpu 0 -batch_size 64 -beam_size 12 \
                            -output "models/lstms2s_${i}_${data_type}.prd" -seed 1
        wait
        python accuracy.py --file1 ../unimorph/${data_type}.tgt --file2 "models/lstms2s_${i}_${data_type}.prd"
        wait
    done
done



