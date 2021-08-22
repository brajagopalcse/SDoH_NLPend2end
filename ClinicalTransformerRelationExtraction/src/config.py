from transformers import (BertConfig, RobertaConfig, XLNetConfig, AlbertConfig, LongformerConfig,
                          BertTokenizer, RobertaTokenizer, XLNetTokenizer, AlbertTokenizer, LongformerTokenizer,
                          DebertaConfig, DebertaTokenizer)
from models import (BertForRelationIdentification, RoBERTaForRelationIdentification,
                    XLNetForRelationIdentification, AlbertForRelationIdentification,
                    LongFormerForRelationIdentification, DebertaForRelationIdentification)


EN1_START = "[s1]"
EN1_END = "[e1]"
EN2_START = "[s2]"
EN2_END = "[e2]"
# keep the seq order
SPEC_TAGS = [EN1_START, EN1_END, EN2_START, EN2_END]

MODEL_REQUIRE_SEGMENT_ID = {'bert', 'xlnet', 'albert', 'deberta'}

MODEL_DICT = {
    "bert": (BertForRelationIdentification, BertConfig, BertTokenizer),
    "roberta": (RoBERTaForRelationIdentification, RobertaConfig, RobertaTokenizer),
    "xlnet": (XLNetForRelationIdentification, XLNetConfig, XLNetTokenizer),
    "albert": (AlbertForRelationIdentification, AlbertConfig, AlbertTokenizer),
    "longformer": (LongFormerForRelationIdentification, LongformerConfig, LongformerTokenizer),
    "deberta": (DebertaForRelationIdentification, DebertaConfig, DebertaTokenizer)
}

TOKENIZER_USE_FOUR_SPECIAL_TOKs = {'roberta', 'longformer'}