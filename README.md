# Dreamboy-Zoo-Genomics-Transformer
dreamboy-zoo-transformer/
│
├── data/                       # O seu zoológico de dados (Não vai pro GitHub!)
│   ├── raw/                    # Sequências brutas (.fasta / .fastq) baixadas do NCBI
│   │   ├── herbivores/         # Rinoceronte, Hipopótamo, Elefante modernos
│   │   ├── carnivores/         # Hiena, Leão, Urso modernos
│   │   ├── cenozoic_herb/      # Paraceratherium, Elasmotherium
│   │   └── cenozoic_carn/      # Daeodon, Dinocrocuta
│   └── processed/              # Seus DNAs já tokenizados e transformados em tensores
│
├── src/                        # Onde a mágica do código acontece
│   ├── __init__.py
│   ├── tokenizer.py            # Transforma as bases A, T, C, G em números (K-mers)
│   ├── dataset.py              # Custom PyTorch Dataset que lê a estrutura das pastas
│   ├── model.py                # Sua arquitetura Transformer (ex: DNABERT adaptado)
│   └── train.py                # Script de treinamento (Diz pro PyTorch rodar na GPU)
│
├── api/                        # Suas rotas do FastAPI
│   └── main.py                 # Endpoint onde você joga um DNA e ele diz o que é
│
├── agents/                     # Seus agentes do CrewAI
│   └── bio_validation.py       # Agentes que validam se o DNA gerado faz sentido
│
├── config.py                   # Caminhos das pastas e hiperparâmetros (Batch size, LR)
├── requirements.txt            # Suas libs: torch, fastapi, crewai, biopython, pydantic
└── README.md                   # Onde você finge ser um cientista sério