% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Aaron Nyholm

```{index} IO Device
```

```{index} iodev
```
# Operations

## Region Mapping

```{code-block} c
int fd;
int status;
size_t count;

fd = open("/dev/iodev0", O_RDWR);
if (fd == 0) {
    return;
}

status = ioctl(fd, RTEMS_IODEV_IOCTL_REGION_COUNT, &count);

if (count > 0) {
    rtems_iodev_region region;
    region.index = 0;

    status = ioctl(fd, RTEMS_IODEV_IOCTL_REGION_GET, &region);
    printf("Region %d: address: %p, size: 0x%x, name: %s\n",
        region.index,
        region.address,
        region.size,
        region.name
    );

    void *addr = mmap(
        NULL,
        region.size,
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        fd,
        region.index
    );
}
```

## Event Usage

```{code-block} c
int fd;
int status;
size_t count;

fd = open("/dev/iodev0", O_RDWR);
if (fd == 0) {
    return;
}

status = ioctl(fd, RTEMS_IODEV_IOCTL_EVENT_COUNT, &count);

if (count > 0) {
    rtems_iodev_event_info info;
    info.index = 0;

    status = ioctl(fd, RTEMS_IODEV_IOCTL_EVENT_INFO, &info);
    printf("Event %d: name: %s\n", info.index, info.name);

    while (true) {
        rtems_iodev_event_args args;
        args.index = 0;
        args.timeout.tv_sec = 0;
        args.timeout.tv_nsec = 0;

        status = ioctl(fd, RTEMS_IODEV_IOCTL_EVENT_WAIT, &args);
        printf("Event %d received\n", args.index);
    }
}
```
