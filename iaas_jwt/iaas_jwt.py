import jwt


def gerador_hs256(sub, nome, apelido, segredo):
    """Gerar um token HS256

    Args:
        sub(str): identificador ou assunto
        nome(str): nome completo do usuário
        apelido(str): apelido do usuário
        segredo(str): senha
    Returns:
        Um dicionário com um token válido
    Examples:
    >>> gerador_hs256(sub='4685',nome='Reinaldo Saraiva', apelido='macewindu', segredo='mypassword')
    {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Njg1Iiwibm9tZSI6IlJlaW5hbGRvIFNhcmFpdmEiLCJhcGVsaWRvIjoibWFjZXdpbmR1In0.UpOrh923u3wYShk_AVolZLCnb43wRS0iAvITQNZ_PLU'}
    """
    payload = {'sub': sub, 'nome': nome, 'apelido': apelido}
    token = jwt.encode(payload=payload, key=segredo)
    return {'token': token}


def gerador_rs256(payload):
    """_summary_

    Args:
        token (str): _description_
        key (str): chave pública
    """
    ...
