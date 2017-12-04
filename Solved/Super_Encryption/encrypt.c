void encrypt(void * block, int edflag) {
    var_78 = block;
    r13 = rsp;
    rsp = rsp - (0xf + edflag) / 0x10 * 0x10;
    var_48 = rsp + 0x0;
    var_80 = 0x0;
    var_34 = 0x0;
    while ((*(int8_t *)(var_78 + sign_extend_64(var_34)) & 0xff) != 0xa) {
            var_80 = var_80 + 0x1;
            rax = *(int8_t *)(var_78 + sign_extend_64(var_34)) & 0xff;
            xmm1 = intrinsic_pxor(xmm1, xmm1);
            xmm1 = intrinsic_cvtsi2sd(xmm1, sign_extend_64(rax));
            var_88 = intrinsic_movsd(var_88, xmm1);
            xmm0 = intrinsic_pxor(xmm0, xmm0);
            xmm0 = intrinsic_cvtsi2sd(xmm0, (SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) - ((SAR(HIDWORD((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - (SAR((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b), 0x1f))) + ((SAR(HIDWORD((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - (SAR((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b), 0x1f)) << 0x2) + ((SAR(HIDWORD((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - (SAR((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b), 0x1f))) + ((SAR(HIDWORD((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - (SAR((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b), 0x1f)) << 0x2) + ((SAR(HIDWORD((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b) * 0x2e8ba2e9), 0x1)) - (SAR((SAR((var_34 + 0x16 >> 0x1f) + var_34 + 0x16, 0x1) ^ 0x1b), 0x1f))));
            rax = floor(xmm0);
            xmm0 = intrinsic_addsd(xmm0, var_88);
            *(int8_t *)(var_48 + sign_extend_32(var_34)) = intrinsic_cvttsd2si(rax, xmm0);
            var_34 = var_34 + 0x1;
    }
    var_34 = 0x0;
    rbx = rsp;
    rsp = rsp - (var_80 + 0xf) / 0x10 * 0x10;
    var_58 = rsp + 0x0;
    while (sign_extend_32(var_34 + 0x4) < var_80) {
            *(int8_t *)(var_58 + sign_extend_32(var_34)) = *(int8_t *)(var_48 + sign_extend_32(var_34 + 0x4)) & 0xff;
            *(int8_t *)(var_58 + sign_extend_64(var_34 + 0x1)) = *(int8_t *)(var_48 + sign_extend_32(var_34 + 0x3)) & 0xff;
            *(int8_t *)(var_58 + sign_extend_64(var_34 + 0x2)) = *(int8_t *)(var_48 + sign_extend_32(var_34 + 0x2)) & 0xff;
            *(int8_t *)(var_58 + sign_extend_64(var_34 + 0x3)) = *(int8_t *)(var_48 + sign_extend_32(var_34 + 0x1)) & 0xff;
            *(int8_t *)(var_58 + sign_extend_64(var_34 + 0x4)) = *(int8_t *)(var_48 + sign_extend_32(var_34)) & 0xff;
            var_34 = var_34 + 0x5;
    }
    while (sign_extend_32(var_34) < var_80) {
            strncpy(sign_extend_32(var_34) + var_58, var_48 + sign_extend_32(var_34), 0x2);
            var_34 = var_34 + 0x1;
    }
    var_34 = 0x0;
    r12 = rsp;
    var_68 = (rsp - (var_80 + 0xf) / 0x10 * 0x10) + 0x0;
    while (sign_extend_32(var_34 + 0x3) < var_80) {
            *(int8_t *)(var_68 + sign_extend_32(var_34)) = *(int8_t *)(var_58 + sign_extend_32(var_34 + 0x2)) & 0xff;
            *(int8_t *)(var_68 + sign_extend_64(var_34 + 0x1)) = *(int8_t *)(var_58 + sign_extend_32(var_34 + 0x1)) & 0xff;
            *(int8_t *)(var_68 + sign_extend_64(var_34 + 0x2)) = *(int8_t *)(var_58 + sign_extend_32(var_34)) & 0xff;
            var_34 = var_34 + 0x3;
    }
    while (sign_extend_32(var_34) < var_80) {
            strncpy(sign_extend_32(var_34) + var_68, var_58 + sign_extend_32(var_34), 0x2);
            var_34 = var_34 + 0x1;
    }
    puts(var_68);
    return;
}