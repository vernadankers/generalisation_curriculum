#!/bin/bash
#SBATCH --job-name=german
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --mem=10000M
#SBATCH -p gpu_shared

module load 2019
module load Python/3.7.5-foss-2019b

python onmt/bin/build_vocab.py -config config/config-german.yml
wait
python train.py -config config/config-unimorph.yml
wait

