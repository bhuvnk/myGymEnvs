from setuptools import setup

setup(name='gym_dabbewala',
      version='0.0.1',
      description='OpenAI Gym environment for a simple navigation and delivery system game',
      author='Bhuvnesh Kumar',
      url="https://github.com/bhuvnk/myGymEnvs",
      install_requires=['gym', 'numpy', 'pygame', 'cv2', 'skimage', 'scipy', 'PIL'],
      python_requires='>=3.6'
)