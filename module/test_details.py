POSSIBLE_TESTS = {
    'connectable': 'SSL/TLS Connection Test',
    'offer_ssl2': 'Offer SSLv2',
    'offer_ssl3': 'Offer SSLv3',
    'offer_tls10': 'Offer TLS1.0',
    'offer_tls11': 'Offer TLS1.1',
    'offer_tls12': 'Offer TLS1.2',
    'heartbleed': 'Heartbleed',
    'ccs_injection': 'CCS Injection',
    'fallback_support': 'TLS_FALLBACK_SCSV Support',
    'poodle_ssl3': 'POODLE (SSLv3)',
    'sweet32': 'SWEET32',
    'drown': 'DROWN',
    'freak': 'FREAK',
    'lucky13' : 'LUCKY13',
    'crime_tls' : 'CRIME (TLS)',
    'breach' : 'BREACH',
    'cipher_NULL' : 'NULL Cipher (no encryption)',
    'cipher_ANON' : 'ANON Cipher (no authentication)',
    'cipher_EXP' : 'EXP Cipher (without ADH+NULL)',
    'cipher_LOW' : 'LOW Cipher (64 Bit + DES Encryption)',
    'cipher_WEAK' : 'WEAK Cipher (SEED, IDEA, RC2, RC4)',
    'cipher_3DES' : '3DES Cipher (Medium)',
    'cipher_HIGH' : 'HIGH Cipher (AES+Camellia, no AEAD)',
    'cipher_STRONG' : 'STRONG Cipher (AEAD Ciphers)'
}

POSSIBLE_RESULTS = {   
    'connectable': ['Failed', 'Successful'],
    'offer_ssl2': ['No', 'Yes (not OK)'],
    'offer_ssl3': ['No', 'Yes (not OK)'],
    'offer_tls10': ['No', 'Yes'],
    'offer_tls11': ['No', 'Yes'],
    'offer_tls12': ['No', 'Yes'],
    'heartbleed': ['Not vulnerable', 'Vulnerable'],
    'ccs_injection': ['Not vulnerable', 'Vulnerable'],
    'fallback_support': ['No', 'Yes'],
    'poodle_ssl3': ['Not vulnerable', 'Vulnerable'],
    'sweet32': ['Not vulnerable', 'Possibly vulnerable'],
    'drown': ['Not vulnerable', 'Vulnerable'],
    'freak': ['Not vulnerable', 'Vulnerable'],
    'lucky13' : ['Not vulnerable', 'Possibly vulnerable'],
    'crime_tls' : ['Not vulnerable', 'Vulnerable'],
    'breach' : ['Not vulnerable', 'Vulnerable'],
    'cipher_NULL' : ['No', 'Yes (not OK)'],
    'cipher_ANON' : ['No', 'Yes (not OK)'],
    'cipher_EXP' : ['No', 'Yes (not OK)'],
    'cipher_LOW' : ['No', 'Yes (not OK)'],
    'cipher_WEAK' : ['No', 'Yes (not OK)'],
    'cipher_3DES' : ['No', 'Yes (not recommended)'],
    'cipher_HIGH' : ['No', 'Yes'],
    'cipher_STRONG' : ['No', 'Yes']   
}