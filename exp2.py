import random


# Helper function to read files
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()


# Helper function to write files
def write_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)


# CRC Implementation
def calculate_crc(data, polynomial=0x1021):
    crc = 0
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFFFF  # Keep it within 16 bits
    return crc


def verify_crc(data, received_crc, polynomial=0x1021):
    calculated_crc = calculate_crc(data, polynomial)
    return calculated_crc == received_crc


# Checksum Implementation
def calculate_checksum(data):
    checksum = sum(data) & 0xFFFF  # 16-bit sum
    return checksum


def verify_checksum(data, received_checksum):
    calculated_checksum = calculate_checksum(data)
    return calculated_checksum == received_checksum


# Simulate file transfer with error
def simulate_transfer(data, error_probability=0.01):
    corrupted_data = bytearray(data)
    for i in range(len(corrupted_data)):
        if random.random() < error_probability:
            corrupted_data[i] ^= 1 << random.randint(0, 7)  # Flip a random bit
    return bytes(corrupted_data)


# Main function for testing
def main():
    file_path = "example.txt"  # Change to your file
    data = read_file(file_path)

    # CRC Demonstration
    print("== CRC Demonstration ==")
    crc = calculate_crc(data)
    print(f"Original CRC: {crc:04X}")
    transferred_data = simulate_transfer(data)
    valid = verify_crc(transferred_data, crc)
    print(f"CRC Valid after transfer: {valid}")

    # Checksum Demonstration
    print("\n== Checksum Demonstration ==")
    checksum = calculate_checksum(data)
    print(f"Original Checksum: {checksum:04X}")
    transferred_data = simulate_transfer(data)
    valid = verify_checksum(transferred_data, checksum)
    print(f"Checksum Valid after transfer: {valid}")


if __name__ == "__main__":
    main()
