void encrypt(char * block, int len) {
    r13 = rsp;
    rsp = rsp - (0xf + len);
    var_48 = rsp + 0x0;
    str_len = 0x0; // to store length of string
    offset = 0x0;
    while ((*(int8_t *)(block + (offset)) & 0xff) != '\n') {
            str_len++;
            rax = *(int8_t *)(block + (offset)) & 0xff;

            xmm1 = 0; // xmm1 = intrinsic_pxor(xmm1, xmm1);
            xmm1 = intrinsic_cvtsi2sd(xmm1, sign_extend_64(rax));
            // get char block[offset]

            var_88 = intrinsic_movsd(var_88, xmm1);
            xmm0 = 0; // xmm0 = intrinsic_pxor(xmm0, xmm0);
            xmm0 = intrinsic_cvtsi2sd(xmm0, 
                (SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) - 
                ((SAR(HIDWORD((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - 
                    (SAR((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b), 0x1f))) + 
                ((SAR(HIDWORD((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - 
                    (SAR((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b), 0x1f)) << 0x2) + 
                ((SAR(HIDWORD((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - 
                    (SAR((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b), 0x1f))) + 
                ((SAR(HIDWORD((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - 
                    (SAR((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b), 0x1f)) << 0x2) + 
                ((SAR(HIDWORD((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - 
                    (SAR((SAR((offset + 0x16 >> 0x1f) + offset + 0x16, 0x1) ^ 0x1b), 0x1f))));
            // The magic constant 0x2E8BA2E9 is used to perform an optimized division by 11

            rax = floor(xmm0);
            xmm0 = intrinsic_addsd(xmm0, var_88);
            // xmm0 = floor(?? / 11)
            // block[offset] = block[offset] + xmm0


            *(int8_t *)(var_48 + sign_extend_32(offset)) = intrinsic_cvttsd2si(rax, xmm0);
            offset++;
    }

    offset = 0;
    rbx = rsp;
    rsp = rsp - (str_len + 0xf);
    var_58 = rsp + 0x0;
    while ((offset + 0x4) < str_len) {
            *(int8_t *)(var_58 + (offset))       = *(int8_t *)(var_48 + (offset + 0x4)) & 0xff;
            *(int8_t *)(var_58 + (offset + 0x1)) = *(int8_t *)(var_48 + (offset + 0x3)) & 0xff;
            *(int8_t *)(var_58 + (offset + 0x2)) = *(int8_t *)(var_48 + (offset + 0x2)) & 0xff;
            *(int8_t *)(var_58 + (offset + 0x3)) = *(int8_t *)(var_48 + (offset + 0x1)) & 0xff;
            *(int8_t *)(var_58 + (offset + 0x4)) = *(int8_t *)(var_48 + (offset)) & 0xff;
            offset += 5;
            // flip the order of every 5 bytes
    }

    while ((offset) < str_len) {
            strncpy(offset + var_58, var_48 + offset, 0x2);
            offset++;
        // left over (not multiple of 5), then copy 2 chars as per normal
    }

    offset = 0x0;
    r12 = rsp;
    var_68 = (rsp - (str_len + 0xf));
    do {
            *(int8_t *)(var_68 + (offset))       = *(int8_t *)(var_58 + (offset + 0x2)) & 0xff;
            *(int8_t *)(var_68 + (offset + 0x1)) = *(int8_t *)(var_58 + (offset + 0x1)) & 0xff;
            *(int8_t *)(var_68 + (offset + 0x2)) = *(int8_t *)(var_58 + (offset)) & 0xff;
            offset += 3;
            // flip order of every 3 bytes
    } while (sign_extend_32(offset) < str_len);

    while (sign_extend_32(offset) < str_len) {
            strncpy(sign_extend_32(offset) + var_68, var_58 + sign_extend_32(offset), 0x2);
            offset += 1;
            // left over copy 2 chars as per normal
    }
    puts(var_68);
    return;
}