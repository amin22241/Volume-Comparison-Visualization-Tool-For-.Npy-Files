from pathlib import Path
import numpy as np
import napari
import json

# add your directory file
base_dir = Path('/Users/subject tests...(replace with your directory)')
file_paths = [base_dir / f'file_{i}.npy' for i in range(5)]

for file in file_paths:
    if not file.exists():
        raise FileNotFoundError(f"File {file} not found.")

volumes = [np.load(file) for file in file_paths]

for i, volume in enumerate(volumes):
    print(f"Volume {i} shape: {volume.shape}")

min_shape = np.min([volume.shape for volume in volumes], axis=0)
volumes = [volume[:min_shape[0], :min_shape[1], :min_shape[2], :min_shape[3]] for volume in volumes]

shapes = [volume.shape for volume in volumes]
if len(set(shapes)) > 1:
    raise ValueError(f"Volumes have inconsistent shapes after cropping: {shapes}")

overlap = np.ones_like(volumes[0])
for volume in volumes:
    overlap *= (volume > 0)

difference = np.abs(volumes[0] - volumes[1])

# overlap and difference 
np.save(base_dir / 'overlap.npy', overlap)
np.save(base_dir / 'difference.npy', difference)
print("Overlap and difference arrays saved as .npy files.")

results = {
    "overlap_shape": overlap.shape,
    "overlap_nonzero_voxels": np.count_nonzero(overlap),
    "difference_shape": difference.shape,
    "difference_mean": float(np.mean(difference)),
    "difference_std": float(np.std(difference)),
}

with open(base_dir / 'results_metadata.json', 'w') as f:
    json.dump(results, f, indent=4)
print("Results metadata saved as JSON.")

# Visualize in napari 
viewer = napari.Viewer()
for i, volume in enumerate(volumes):
    viewer.add_image(volume, name=f'Volume {i}', colormap='gray', blending='additive')

viewer.add_image(overlap, name='Overlap', colormap='green', blending='additive', opacity=0.5)
viewer.add_image(difference, name='Difference', colormap='red', blending='additive', opacity=0.5)

screenshot = viewer.screenshot()
import imageio
imageio.imwrite(base_dir / 'napari_screenshot.png', screenshot)
print("Screenshot saved.")

napari.run()