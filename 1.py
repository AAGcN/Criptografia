import base64

decoded = base64.b64decode('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')
keylength = 10

# Se hacen bloques del cyphertext segun la longitud de la clave
def transpose_chunks_by_keylength(keylength, ciphertext):
  chunks = {chunk:[] for chunk in range(keylength)}

  i = 0
  for octet in ciphertext:
    if (i == keylength): i = 0

    chunks[i].append(octet)

    i += 1

  return chunks

# Se hacen grupos con los bytes de cada bloque, se realiza la busqueda y se le añade un analisis
# de frecuencia con puntuacion
def get_key(blocks):
  common = 'ETAOIN SHRDLU'
  key = ''

  for i in blocks:
    current_high_score = 0
    current_key_char = ''

    for j in range(128):
      x = [j ^ the_bytes for the_bytes in blocks[i]]
      b = bytes(x)
      b_str = str(b, 'utf-8')

      score = 0
      for k in b_str.upper():
          if k in common:
              score += 1

      if score > current_high_score:
        current_high_score = score
        current_key_char = chr(j)

    key += current_key_char

  print('Key = ', key)
  return key

def decrypt(message_bytes, key):
  decrypted = b''

  i = 0
  for byte in message_bytes:
    if (i == len(key)):
      i = 0

    xor = byte ^ ord(key[i])
    decrypted += bytes([xor])

    i += 1
  
  print('The encrypted message = ', decrypted)
  return decrypted


chunks = transpose_chunks_by_keylength(keylength, decoded)
key = get_key(chunks)
decrypted = decrypt(decoded, key)