from ipywidgets import widgets
from IPython.display import display
import warnings
warnings.filterwarnings("ignore")

box = widgets.FloatSlider(min=5, max=12, step=0.5, value=6.0, description='Box size')
solvent	= widgets.Dropdown(options=['W', 'EOL', 'OD'], value='W', description='Solvent')
nlip = widgets.IntSlider(min=10, max=150, value=50, description='# of lipids')
lipid = widgets.Dropdown(options=['CPC',
                                  'DLPC',
                                  'DOPC',
                                  'DPGS',
                                  'DPPC',
                                  'DPPG',
                                  'DPSM',
                                  'DTPC',
                                  'DTPE',
                                  'DTPG',
                                  'DTPS',
                                  'DXCE',
                                  'DXPE',
                                  'LPC',
                                  'PADG',
                                  'POPC',
                                  'POPE',
                                  'POPG',
                                  'PPC',
                                  'PRPC',
                                  'PRPS',
                                  'PVDG'],
                                  value='DPPC', description='Lipid')

display(lipid)
display(solvent)
display(nlip)
display(box)
