from setuptools import setup, find_packages


VERSION = '1.0.0' 
DESCRIPTION = 'DDM microscopy package for educational purpose.'
LONG_DESCRIPTION = 'DDM microscopy package for educational purpose. For an efficient software solution, see simd-ddm.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ddm-edu", 
        version=VERSION,
        author="Erwan Le Doeuff, weld",
        author_email="<erwan.le-doeuff@etu.umontpellier.fr>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        package_data={'': ['libddm.so']},
        packages=find_packages(),
        install_requires=['numpy', 'tifffile'],
    
        keywords=['python', 'ddm', 'microscopy'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X"
        ]
)
