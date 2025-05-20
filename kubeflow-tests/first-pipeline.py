import kfp
from kfp import dsl
import pandas as pd

# Etape 1: Créer un DataFrame simple
@dsl.component
def create_dataframe_op() -> dict:
    # Créer un DataFrame simple avec pandas
    data = {'Nom': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    # Convertir le DataFrame en dictionnaire avant de le renvoyer
    return df.to_dict()

# Etape 2: Afficher le DataFrame
@dsl.component
def print_dataframe_op(df: dict):
    # Convertir le dictionnaire en DataFrame pour l'affichage
    df_pd = pd.DataFrame(df)
    print("Voici le DataFrame généré :")
    print(df_pd)

# Définir le pipeline
@dsl.pipeline(
    name='Simple DataFrame Pipeline',
    description='Un pipeline simple qui génère et affiche un DataFrame.'
)
def simple_dataframe_pipeline():
    # Etape 1: Créer un DataFrame
    df = create_dataframe_op()
    
    # Etape 2: Afficher le DataFrame (en utilisant des arguments nommés)
    print_dataframe_op(df=df.output)

# Compiler le pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_dataframe_pipeline, 'simple_dataframe_pipeline.yaml')

