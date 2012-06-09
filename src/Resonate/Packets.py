import Types

structures = []

#Keep Alive (0x00)
structures[0x00] = (Types.Integer)

#Login Request (0x01)
structures[0x01] = (Types.Integer, Types.String, Types.String, Types.Integer, Types.Integer, Types.Byte, Types.UnsignedByte, Types.UnsignedByte)

#Handshake (0x02)
structures[0x02] = (Types.String)

#Chat Message (0x03)
structures[0x03] = (Types.String)

#Time Update (0x04)
structures[0x04] = (Types.Long)

#Entity Equipment (0x05)
structures[0x05] = (Types.Integer, Types.Short, Types.Short, Types.Short)

#Spawn Position (0x06)
structures[0x06] = (Types.Integer, Types.Integer, Types.Integer)

#Use Entity (0x07)
structures[0x07] = (Types.Integer, Types.Integer, Types.Bool)

#Update Health (0x08)
structures[0x08] = (Types.Short, Types.Short, Types.Float)

#Respawn (0x09)
structures[0x09] = (Types.Integer, Types.Byte, Types.Byte, Types.Short, Types.String)

#Player (0x0A)
structures[0x0A] = (Types.Bool)

#Player Position (0x0B)
structures[0x0B] = (Types.Double, Types.Double, Types.Double, Types.Double, Types.Bool)

#Player Look (0x0C)
structures[0x0C] = (Types.Float, Types.Float, Types.Bool)

#Player Position & Look (0x0D)
structures[0x0D] = (Types.Double, Types.Double, Types.Double, Types.Double, Types.Float, Types.Float, Types.Bool)

#Player Digging (0x0E)
structures[0x0E] = (Types.Byte, Types.Integer, Types.Byte, Types.Integer, Types.Byte)

#Player Block Placement (0x0F)
structures[0x0F] = (Types.Integer, Types.UnsignedByte, Types.Integer, Types.Byte, '*slot*')

#Held Item Change (0x10)
structures[0x10] = (Types.Short)

#Use Bed (0x11)
structures[0x11] = (Types.Integer, Types.Byte, Types.Integer, Types.Byte, Types.Integer)

#Animation (0x12)
structures[0x12] = (Types.Integer, Types.Byte)

#Entity Action (0x13)
structures[0x13] = (Types.Integer, Types.Byte)

#Spawn Named Entity (0x14)
structures[0x14] = (Types.Integer, Types.String, Types.Integer, Types.Integer, Types.Integer, Types.Byte, Types.Byte, Types.Short)

#Spawn Dropped Item (0x15)
structures[0x15] = (Types.Integer, Types.Short, Types.Byte, Types.Short, Types.Integer, Types.Integer, Types.Integer, Types.Byte, Types.Byte, Types.Byte)

#Collect Item (0x16)
structures[0x16] = (Types.Integer, Types.Integer)

#Spawn Object/Vehicle (0x17)
structures[0x17] = (Types.Integer, Types.Byte, Types.Integer, Types.Integer, Types.Integer, Types.Integer, Types.Short, Types.Short, Types.Short)

#Spawn Mob (0x18)
structures[0x18] = (Types.Integer, Types.Byte, Types.Integer, Types.Integer, Types.Integer, Types.Byte, Types.Byte, Types.Byte, Types.Metadata)

#Spawn Painting (0x19)
structures[0x19] = (Types.Integer, Types.String, Types.Integer, Types.Integer, Types.Integer, Types.Integer)

#Spawn Experience Orb (0x1A)
structures[0x1A] = (Types.Integer, Types.Integer, Types.Integer, Types.Integer, Types.Short)

#Entity Velocity (0x1C)
structures[0x1C] = (Types.Integer, Types.Short, Types.Short, Types.Short)

#Destroy Entity (0x1D)
structures[0x1D] = (Types.Integer)

#Entity (0x1E)
structures[0x1E] = (Types.Integer)

#Entity Relative Move (0x1F)
structures[0x1F] = (Types.Integer, Types.Byte, Types.Byte, Types.Byte)

#Entity Look (0x20)
structures[0x20] = (Types.Integer, Types.Byte, Types.Byte)

#Entity Look and Relative Move (0x21)
structures[0x21] = (Types.Integer, Types.Byte, Types.Byte, Types.Byte, Types.Byte, Types.Byte)

#Entity Teleport (0x22)
structures[0x22] = (Types.Integer, Types.Integer, Types.Integer, Types.Integer, Types.Byte, Types.Byte)

#Entity Head Look (0x23)
structures[0x23] = (Types.Integer, Types.Byte)

#Entity Status (0x26)
structures[0x26] = (Types.Integer, Types.Byte)

#Attach Entity (0x27)
structures[0x27] = (Types.Integer, Types.Integer)

#Entity Metadata (0x28)
structures[0x28] = (Types.Integer, Types.Metadata)

#Entity Effect (0x29)
structures[0x29] = (Types.Integer, Types.Byte, Types.Byte, Types.Short)

#Remove Entity Effect (0x2A)
structures[0x2A] = (Types.Integer, Types.Byte)

#Set Experience (0x2B)
structures[0x2B] = (Types.Float, Types.Short, Types.Short)

#Map Column Allocation (0x32)
structures[0x32] = (Types.Integer, Types.Integer, Types.Bool)

#Map Chunks (0x33)
structures[0x33] = (Types.Integer, Types.Integer, Types.Bool, Types.UnsignedShort, Types.UnsignedShort, Types.Integer, Types.Integer, '*unsigned byte array*')

#Multi Block Change (0x34)
structures[0x34] = (Types.Integer, Types.Integer, Types.Short, Types.Integer, '**')

#Block Change (0x35)
structures[0x35] = (Types.Integer, Types.Byte, Types.Integer, Types.Byte, Types.Byte)

#Block Action (0x36)
structures[0x36] = ()

#Explosion (0x3C)
structures[0x3C] = (Types.Double, Types.Double, Types.Double, Types.Float, Types.Integer, '*(byte, byte, byte) ã— count*')

#Sound/Particle Effect (0x3D)
structures[0x3D] = (Types.Integer, Types.Integer, Types.Byte, Types.Integer, Types.Integer)

#Change Game State (0x46)
structures[0x46] = (Types.Byte, Types.Byte)

#Thunderbolt (0x47)
structures[0x47] = (Types.Integer, Types.Bool, Types.Integer, Types.Integer, Types.Integer)

#Open Window (0x64)
structures[0x64] = (Types.Byte, Types.Byte, Types.String, Types.Byte)

#Close Window (0x65)
structures[0x65] = (Types.Byte)

#Click Window (0x66)
structures[0x66] = (Types.Byte, Types.Short, Types.Byte, Types.Short, Types.Bool, '*slot*')

#Set Slot (0x67)
structures[0x67] = (Types.Byte, Types.Short, '*slot*')

#Set Window Items (0x68)
structures[0x68] = (Types.Byte, Types.Short, '*array of slots*')

#Update Window Property (0x69)
structures[0x69] = (Types.Byte, Types.Short, Types.Short)

#Confirm Transaction (0x6A)
structures[0x6A] = (Types.Byte, Types.Short, Types.Bool)

#Creative Inventory Action (0x6B)
structures[0x6B] = (Types.Short, '*slot*')

#Enchant Item (0x6C)
structures[0x6C] = (Types.Byte, Types.Byte)

#Update Sign (0x82)
structures[0x82] = (Types.Integer, Types.Short, Types.Integer, Types.String, Types.String, Types.String, Types.String)

#Item Data (0x83)
structures[0x83] = (Types.Short, Types.Short, Types.UnsignedByte, '*byte array*')

#Update Tile Entity (0x84)
structures[0x84] = (Types.Integer, Types.Short, Types.Integer, Types.Byte, Types.Integer, Types.Integer, Types.Integer)

#Increment Statistic (0xC8)
structures[0xC8] = (Types.Integer, Types.Byte)

#Player List Item (0xC9)
structures[0xC9] = (Types.String, Types.Bool, Types.Short)

#Player Abilities (0xCA)
structures[0xCA] = (Types.Bool, Types.Bool, Types.Bool, Types.Bool)

#Plugin Message (0xFA)
structures[0xFA] = (Types.String, Types.Short, '*byte array*')

#Server List Ping (0xFE)
structures[0xFE] = ()

#Disconnect/Kick (0xFF)
structures[0xFF] = (Types.String)

