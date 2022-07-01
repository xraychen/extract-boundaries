import torch
import numpy as np
import pandas as pd
from tqdm import tqdm
import os
import torchaudio

import argparse


def extract_boundaries(args, feat_paths):
    """Extract boundaries"""
    for feat_path in tqdm(feat_paths):
        out_filename = os.path.join(args.output_dir, feat_path.split(".")[0] + ".npy")

        wav, _ = torchaudio.load(os.path.join(args.libri_root, feat_path))
        """Extract boundaries of wav"""

        boundaries = None # array of boundaries time stamps or the index according to 20ms sample rate
        raise NotImplementedError

        boundaries = boundaries.cpu().detach().numpy()

        os.makedirs(
            os.path.join(
                args.output_dir, "/".join(feat_path.split(".")[0].split("/")[:-1])
            ),
            exist_ok=True,
        )
        out_filename = os.path.join(args.output_dir, feat_path.split(".")[0] + ".npy")
        np.save(out_filename, boundaries)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
       "--libri_root", type=str, default="/groups/public/LibriSpeech"
    )
    parser.add_argument(
        "--len_for_bucket", type=str, default="./len_for_bucket"
    )
    parser.add_argument(
        "--sets",
        type=str,
        default="train-clean-100,train-clean-360,train-other-500,dev-clean,dev-other,test-clean,test-other",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./boundaries"
    )

    return parser.parse_args()


def main():
    args = get_args()
    print(args)

    # feat_paths
    file_path = args.len_for_bucket
    sets = args.sets.split(",")
    print(f"Extracting {sets}")

    tables = [pd.read_csv(os.path.join(file_path, s + ".csv")) for s in sets]
    table = pd.concat(tables, ignore_index=True).sort_values(
        by=["length"], ascending=False
    )
    feat_paths = table["file_path"].tolist()

    print(f"Total number of audio is: {len(feat_paths)}")

    extract_boundaries(args, feat_paths)


if __name__ == "__main__":
    main()
