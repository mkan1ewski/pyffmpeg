# --- AUTO-GENERATED FILE ---
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from pyffmpeg.node import Stream, FilterMultiOutput, SinkNode


class GeneratedFiltersMixin:
    """
    Mixin class containing auto-generated filter methods.
    This class should be inherited by the Stream class.
    """

    def a3dscope(
        self,
        rate: str | None = None,
        r: str | None = None,
        size: str | None = None,
        s: str | None = None,
        fov: float | None = None,
        roll: float | None = None,
        pitch: float | None = None,
        yaw: float | None = None,
        xzoom: float | None = None,
        yzoom: float | None = None,
        zzoom: float | None = None,
        xpos: float | None = None,
        ypos: float | None = None,
        zpos: float | None = None,
        length: int | None = None,
    ) -> "Stream":
        """Convert input audio to 3d scope video output.

        Args:
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            size (str): set video size

                Defaults to hd720.
            s (str): set video size

                Defaults to hd720.
            fov (float): set camera FoV (from 40 to 150)

                Defaults to 90.
            roll (float): set camera roll (from -180 to 180)

                Defaults to 0.
            pitch (float): set camera pitch (from -180 to 180)

                Defaults to 0.
            yaw (float): set camera yaw (from -180 to 180)

                Defaults to 0.
            xzoom (float): set camera zoom (from 0.01 to 10)

                Defaults to 1.
            yzoom (float): set camera zoom (from 0.01 to 10)

                Defaults to 1.
            zzoom (float): set camera zoom (from 0.01 to 10)

                Defaults to 1.
            xpos (float): set camera position (from -60 to 60)

                Defaults to 0.
            ypos (float): set camera position (from -60 to 60)

                Defaults to 0.
            zpos (float): set camera position (from -60 to 60)

                Defaults to 0.
            length (int): set length (from 1 to 60)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="a3dscope",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "fov": fov,
                "roll": roll,
                "pitch": pitch,
                "yaw": yaw,
                "xzoom": xzoom,
                "yzoom": yzoom,
                "zzoom": zzoom,
                "xpos": xpos,
                "ypos": ypos,
                "zpos": zpos,
                "length": length,
            },
        )[0]

    def aap(
        self,
        desired_stream: "Stream",
        order: int | None = None,
        projection: int | None = None,
        mu: float | None = None,
        delta: float | None = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "Stream":
        """Apply Affine Projection algorithm to first audio stream.

        Args:
            desired_stream (Stream): Input audio stream.
            order (int): set the filter order (from 1 to 32767)

                Defaults to 16.
            projection (int): set the filter projection (from 1 to 256)

                Defaults to 2.
            mu (float): set the filter mu (from 0 to 1)

                Defaults to 0.0001.
            delta (float): set the filter delta (from 0 to 1)

                Defaults to 0.001.
            out_mode (int | str): set output mode (from 0 to 4)

                Allowed values:
                    * i: input
                    * d: desired
                    * o: output
                    * n: noise
                    * e: error

                Defaults to o.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aap",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "projection": projection,
                "mu": mu,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def abench(self, action: Literal["start", "stop"] | int | None = None) -> "Stream":
        """Benchmark part of a filtergraph.

        Args:
            action (int | str): set action (from 0 to 1)

                Allowed values:
                    * start: start timer
                    * stop: stop timer

                Defaults to start.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="abench",
            inputs=[self],
            named_arguments={
                "action": action,
            },
        )[0]

    def abitscope(
        self,
        rate: str | None = None,
        r: str | None = None,
        size: str | None = None,
        s: str | None = None,
        colors: str | None = None,
        mode: Literal["bars", "trace"] | int | None = None,
        m: Literal["bars", "trace"] | int | None = None,
    ) -> "Stream":
        """Convert input audio to audio bit scope video output.

        Args:
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            size (str): set video size

                Defaults to 1024x256.
            s (str): set video size

                Defaults to 1024x256.
            colors (str): set channels colors

                Defaults to red|green|blue|yellow|orange|lime|pink|magenta|brown.
            mode (int | str): set output mode (from 0 to 1)

                Allowed values:
                    * bars
                    * trace

                Defaults to bars.
            m (int | str): set output mode (from 0 to 1)

                Allowed values:
                    * bars
                    * trace

                Defaults to bars.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="abitscope",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "colors": colors,
                "mode": mode,
                "m": m,
            },
        )[0]

    def abuffersink(
        self,
        sample_fmts: str | None = None,
        sample_rates: str | None = None,
        ch_layouts: str | None = None,
        all_channel_counts: Literal["sample_formats", "samplerates", "channel_layouts"]
        | None = None,
    ) -> "SinkNode":
        """Buffer audio frames, and make them available to the end of the filter graph.

        Args:
            sample_fmts (str): set the supported sample formats

            sample_rates (str): set the supported sample rates

            ch_layouts (str): set a '|'-separated list of supported channel layouts

            all_channel_counts (bool): accept all channel counts

                Allowed values:
                    * sample_formats: of supported sample formats
                    * samplerates: array of supported sample formats
                    * channel_layouts: of supported channel layouts

                Defaults to false.

        Returns:
            "SinkNode": A SinkNode representing the sink (terminal node).
        """
        return self._apply_sink_filter(
            filter_name="abuffersink",
            inputs=[self],
            named_arguments={
                "sample_fmts": sample_fmts,
                "sample_rates": sample_rates,
                "ch_layouts": ch_layouts,
                "all_channel_counts": all_channel_counts,
            },
        )

    def acompressor(
        self,
        level_in: float | None = None,
        mode: Literal["downward", "upward"] | int | None = None,
        threshold: float | None = None,
        ratio: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        makeup: float | None = None,
        knee: float | None = None,
        link: Literal["average", "maximum"] | int | None = None,
        detection: Literal["peak", "rms"] | int | None = None,
        level_sc: float | None = None,
        mix: float | None = None,
    ) -> "Stream":
        """Audio compressor.

        Args:
            level_in (float): set input gain (from 0.015625 to 64)

                Defaults to 1.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * downward
                    * upward

                Defaults to downward.
            threshold (float): set threshold (from 0.000976563 to 1)

                Defaults to 0.125.
            ratio (float): set ratio (from 1 to 20)

                Defaults to 2.
            attack (float): set attack (from 0.01 to 2000)

                Defaults to 20.
            release (float): set release (from 0.01 to 9000)

                Defaults to 250.
            makeup (float): set make up gain (from 1 to 64)

                Defaults to 1.
            knee (float): set knee (from 1 to 8)

                Defaults to 2.82843.
            link (int | str): set link type (from 0 to 1)

                Allowed values:
                    * average
                    * maximum

                Defaults to average.
            detection (int | str): set detection (from 0 to 1)

                Allowed values:
                    * peak
                    * rms

                Defaults to rms.
            level_sc (float): set sidechain gain (from 0.015625 to 64)

                Defaults to 1.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acompressor",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "link": link,
                "detection": detection,
                "level_sc": level_sc,
                "mix": mix,
            },
        )[0]

    def acontrast(self, contrast: float | None = None) -> "Stream":
        """Simple audio dynamic range compression/expansion filter.

        Args:
            contrast (float): set contrast (from 0 to 100)

                Defaults to 33.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acontrast",
            inputs=[self],
            named_arguments={
                "contrast": contrast,
            },
        )[0]

    def acopy(
        self,
    ) -> "Stream":
        """Copy the input audio unchanged to the output.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acopy", inputs=[self], named_arguments={}
        )[0]

    def acrossfade(
        self,
        crossfade1_stream: "Stream",
        nb_samples: str | None = None,
        ns: str | None = None,
        duration: str | None = None,
        d: str | None = None,
        overlap: bool | None = None,
        o: bool | None = None,
        curve1: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
        c1: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
        curve2: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
        c2: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Cross fade two input audio streams.

        Args:
            crossfade1_stream (Stream): Input audio stream.
            nb_samples (str): set number of samples for cross fade duration (from 1 to 2.14748e+08)

                Defaults to 44100.
            ns (str): set number of samples for cross fade duration (from 1 to 2.14748e+08)

                Defaults to 44100.
            duration (str): set cross fade duration

                Defaults to 0.
            d (str): set cross fade duration

                Defaults to 0.
            overlap (bool): overlap 1st stream end with 2nd stream start

                Defaults to true.
            o (bool): overlap 1st stream end with 2nd stream start

                Defaults to true.
            curve1 (int | str): set fade curve type for 1st stream (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.
            c1 (int | str): set fade curve type for 1st stream (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.
            curve2 (int | str): set fade curve type for 2nd stream (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.
            c2 (int | str): set fade curve type for 2nd stream (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acrossfade",
            inputs=[self, crossfade1_stream],
            named_arguments={
                "nb_samples": nb_samples,
                "ns": ns,
                "duration": duration,
                "d": d,
                "overlap": overlap,
                "o": o,
                "curve1": curve1,
                "c1": c1,
                "curve2": curve2,
                "c2": c2,
            },
        )[0]

    def acrossover(
        self,
        split: str | None = None,
        order: Literal[
            "2nd", "4th", "6th", "8th", "10th", "12th", "14th", "16th", "18th", "20th"
        ]
        | int
        | None = None,
        level: float | None = None,
        gain: str | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "FilterMultiOutput":
        """Split audio into per-bands streams.

        Args:
            split (str): set split frequencies

                Defaults to 500.
            order (int | str): set filter order (from 0 to 9)

                Allowed values:
                    * 2nd: 2nd order (12 dB/8ve)
                    * 4th: 4th order (24 dB/8ve)
                    * 6th: 6th order (36 dB/8ve)
                    * 8th: 8th order (48 dB/8ve)
                    * 10th: 10th order (60 dB/8ve)
                    * 12th: 12th order (72 dB/8ve)
                    * 14th: 14th order (84 dB/8ve)
                    * 16th: 16th order (96 dB/8ve)
                    * 18th: 18th order (108 dB/8ve)
                    * 20th: 20th order (120 dB/8ve)

                Defaults to 4th.
            level (float): set input gain (from 0 to 1)

                Defaults to 1.
            gain (str): set output bands gain

                Defaults to 1.f.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="acrossover",
            inputs=[self],
            named_arguments={
                "split": split,
                "order": order,
                "level": level,
                "gain": gain,
                "precision": precision,
            },
        )

    def acrusher(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        bits: float | None = None,
        mix: float | None = None,
        mode: Literal["lin", "log"] | int | None = None,
        dc: float | None = None,
        aa: float | None = None,
        samples: float | None = None,
        lfo: bool | None = None,
        lforange: float | None = None,
        lforate: float | None = None,
    ) -> "Stream":
        """Reduce audio bit resolution.

        Args:
            level_in (float): set level in (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set level out (from 0.015625 to 64)

                Defaults to 1.
            bits (float): set bit reduction (from 1 to 64)

                Defaults to 8.
            mix (float): set mix (from 0 to 1)

                Defaults to 0.5.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: logarithmic

                Defaults to lin.
            dc (float): set DC (from 0.25 to 4)

                Defaults to 1.
            aa (float): set anti-aliasing (from 0 to 1)

                Defaults to 0.5.
            samples (float): set sample reduction (from 1 to 250)

                Defaults to 1.
            lfo (bool): enable LFO

                Defaults to false.
            lforange (float): set LFO depth (from 1 to 250)

                Defaults to 20.
            lforate (float): set LFO rate (from 0.01 to 200)

                Defaults to 0.3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acrusher",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "bits": bits,
                "mix": mix,
                "mode": mode,
                "dc": dc,
                "aa": aa,
                "samples": samples,
                "lfo": lfo,
                "lforange": lforange,
                "lforate": lforate,
            },
        )[0]

    def acue(
        self,
        cue: str | None = None,
        preroll: str | None = None,
        buffer: str | None = None,
    ) -> "Stream":
        """Delay filtering to match a cue.

        Args:
            cue (str): cue unix timestamp in microseconds (from 0 to I64_MAX)

                Defaults to 0.
            preroll (str): preroll duration in seconds

                Defaults to 0.
            buffer (str): buffer duration in seconds

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="acue",
            inputs=[self],
            named_arguments={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            },
        )[0]

    def addroi(
        self,
        x: str | None = None,
        y: str | None = None,
        w: str | None = None,
        h: str | None = None,
        qoffset: str | None = None,
        clear: bool | None = None,
    ) -> "Stream":
        """Add region of interest to frame.

        Args:
            x (str): Region distance from left edge of frame.

                Defaults to 0.
            y (str): Region distance from top edge of frame.

                Defaults to 0.
            w (str): Region width.

                Defaults to 0.
            h (str): Region height.

                Defaults to 0.
            qoffset (str): Quantisation offset to apply in the region. (from -1 to 1)

                Defaults to -1/10.
            clear (bool): Remove any existing regions of interest before adding the new one.

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="addroi",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "qoffset": qoffset,
                "clear": clear,
            },
        )[0]

    def adeclick(
        self,
        window: float | None = None,
        w: float | None = None,
        overlap: float | None = None,
        o: float | None = None,
        arorder: float | None = None,
        a: float | None = None,
        threshold: float | None = None,
        t: float | None = None,
        burst: float | None = None,
        b: float | None = None,
        method: Literal["add", "a", "save", "s"] | int | None = None,
        m: Literal["add", "a", "save", "s"] | int | None = None,
    ) -> "Stream":
        """Remove impulsive noise from input audio.

        Args:
            window (float): set window size (from 10 to 100)

                Defaults to 55.
            w (float): set window size (from 10 to 100)

                Defaults to 55.
            overlap (float): set window overlap (from 50 to 95)

                Defaults to 75.
            o (float): set window overlap (from 50 to 95)

                Defaults to 75.
            arorder (float): set autoregression order (from 0 to 25)

                Defaults to 2.
            a (float): set autoregression order (from 0 to 25)

                Defaults to 2.
            threshold (float): set threshold (from 1 to 100)

                Defaults to 2.
            t (float): set threshold (from 1 to 100)

                Defaults to 2.
            burst (float): set burst fusion (from 0 to 10)

                Defaults to 2.
            b (float): set burst fusion (from 0 to 10)

                Defaults to 2.
            method (int | str): set overlap method (from 0 to 1)

                Allowed values:
                    * add: overlap-add
                    * a: overlap-add
                    * save: overlap-save
                    * s: overlap-save

                Defaults to add.
            m (int | str): set overlap method (from 0 to 1)

                Allowed values:
                    * add: overlap-add
                    * a: overlap-add
                    * save: overlap-save
                    * s: overlap-save

                Defaults to add.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adeclick",
            inputs=[self],
            named_arguments={
                "window": window,
                "w": w,
                "overlap": overlap,
                "o": o,
                "arorder": arorder,
                "a": a,
                "threshold": threshold,
                "t": t,
                "burst": burst,
                "b": b,
                "method": method,
                "m": m,
            },
        )[0]

    def adeclip(
        self,
        window: float | None = None,
        w: float | None = None,
        overlap: float | None = None,
        o: float | None = None,
        arorder: float | None = None,
        a: float | None = None,
        threshold: float | None = None,
        t: float | None = None,
        hsize: int | None = None,
        n: int | None = None,
        method: Literal["add", "a", "save", "s"] | int | None = None,
        m: Literal["add", "a", "save", "s"] | int | None = None,
    ) -> "Stream":
        """Remove clipping from input audio.

        Args:
            window (float): set window size (from 10 to 100)

                Defaults to 55.
            w (float): set window size (from 10 to 100)

                Defaults to 55.
            overlap (float): set window overlap (from 50 to 95)

                Defaults to 75.
            o (float): set window overlap (from 50 to 95)

                Defaults to 75.
            arorder (float): set autoregression order (from 0 to 25)

                Defaults to 8.
            a (float): set autoregression order (from 0 to 25)

                Defaults to 8.
            threshold (float): set threshold (from 1 to 100)

                Defaults to 10.
            t (float): set threshold (from 1 to 100)

                Defaults to 10.
            hsize (int): set histogram size (from 100 to 9999)

                Defaults to 1000.
            n (int): set histogram size (from 100 to 9999)

                Defaults to 1000.
            method (int | str): set overlap method (from 0 to 1)

                Allowed values:
                    * add: overlap-add
                    * a: overlap-add
                    * save: overlap-save
                    * s: overlap-save

                Defaults to add.
            m (int | str): set overlap method (from 0 to 1)

                Allowed values:
                    * add: overlap-add
                    * a: overlap-add
                    * save: overlap-save
                    * s: overlap-save

                Defaults to add.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adeclip",
            inputs=[self],
            named_arguments={
                "window": window,
                "w": w,
                "overlap": overlap,
                "o": o,
                "arorder": arorder,
                "a": a,
                "threshold": threshold,
                "t": t,
                "hsize": hsize,
                "n": n,
                "method": method,
                "m": m,
            },
        )[0]

    def adecorrelate(
        self, stages: int | None = None, seed: str | None = None
    ) -> "Stream":
        """Apply decorrelation to input audio.

        Args:
            stages (int): set filtering stages (from 1 to 16)

                Defaults to 6.
            seed (str): set random seed (from -1 to UINT32_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adecorrelate",
            inputs=[self],
            named_arguments={
                "stages": stages,
                "seed": seed,
            },
        )[0]

    def adelay(self, delays: str | None = None, all: bool | None = None) -> "Stream":
        """Delay one or more audio channels.

        Args:
            delays (str): set list of delays for each channel

            all (bool): use last available delay for remained channels

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adelay",
            inputs=[self],
            named_arguments={
                "delays": delays,
                "all": all,
            },
        )[0]

    def adenorm(
        self,
        level: float | None = None,
        type: Literal["dc", "ac", "square", "pulse"] | int | None = None,
    ) -> "Stream":
        """Remedy denormals by adding extremely low-level noise.

        Args:
            level (float): set level (from -451 to -90)

                Defaults to -351.
            type (int | str): set type (from 0 to 3)

                Allowed values:
                    * dc
                    * ac
                    * square
                    * pulse

                Defaults to dc.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adenorm",
            inputs=[self],
            named_arguments={
                "level": level,
                "type": type,
            },
        )[0]

    def aderivative(
        self,
    ) -> "Stream":
        """Compute derivative of input audio.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aderivative", inputs=[self], named_arguments={}
        )[0]

    def adrawgraph(
        self,
        m1: str | None = None,
        fg1: str | None = None,
        m2: str | None = None,
        fg2: str | None = None,
        m3: str | None = None,
        fg3: str | None = None,
        m4: str | None = None,
        fg4: str | None = None,
        bg: str | None = None,
        min: float | None = None,
        max: float | None = None,
        mode: Literal["bar", "dot", "line"] | int | None = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | int
        | None = None,
        size: str | None = None,
        s: str | None = None,
        rate: str | None = None,
        r: str | None = None,
    ) -> "Stream":
        """Draw a graph using input audio metadata.

        Args:
            m1 (str): set 1st metadata key

            fg1 (str): set 1st foreground color expression

                Defaults to 0xffff0000.
            m2 (str): set 2nd metadata key

            fg2 (str): set 2nd foreground color expression

                Defaults to 0xff00ff00.
            m3 (str): set 3rd metadata key

            fg3 (str): set 3rd foreground color expression

                Defaults to 0xffff00ff.
            m4 (str): set 4th metadata key

            fg4 (str): set 4th foreground color expression

                Defaults to 0xffffff00.
            bg (str): set background color

                Defaults to white.
            min (float): set minimal value (from INT_MIN to INT_MAX)

                Defaults to -1.
            max (float): set maximal value (from INT_MIN to INT_MAX)

                Defaults to 1.
            mode (int | str): set graph mode (from 0 to 2)

                Allowed values:
                    * bar: draw bars
                    * dot: draw dots
                    * line: draw lines

                Defaults to line.
            slide (int | str): set slide mode (from 0 to 4)

                Allowed values:
                    * frame: draw new frames
                    * replace: replace old columns with new
                    * scroll: scroll from right to left
                    * rscroll: scroll from left to right
                    * picture: display graph in single frame

                Defaults to frame.
            size (str): set graph size

                Defaults to 900x256.
            s (str): set graph size

                Defaults to 900x256.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adrawgraph",
            inputs=[self],
            named_arguments={
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "bg": bg,
                "min": min,
                "max": max,
                "mode": mode,
                "slide": slide,
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
            },
        )[0]

    def adrc(
        self,
        transfer: str | None = None,
        attack: float | None = None,
        release: float | None = None,
        channels: str | None = None,
    ) -> "Stream":
        """Audio Spectral Dynamic Range Controller.

        Args:
            transfer (str): set the transfer expression

                Defaults to p.
            attack (float): set the attack (from 1 to 1000)

                Defaults to 50.
            release (float): set the release (from 5 to 2000)

                Defaults to 100.
            channels (str): set channels to filter

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adrc",
            inputs=[self],
            named_arguments={
                "transfer": transfer,
                "attack": attack,
                "release": release,
                "channels": channels,
            },
        )[0]

    def adynamicequalizer(
        self,
        threshold: float | None = None,
        dfrequency: float | None = None,
        dqfactor: float | None = None,
        tfrequency: float | None = None,
        tqfactor: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        ratio: float | None = None,
        makeup: float | None = None,
        range: float | None = None,
        mode: Literal["listen", "cutbelow", "cutabove", "boostbelow", "boostabove"]
        | int
        | None = None,
        dftype: Literal["bandpass", "lowpass", "highpass", "peak"] | int | None = None,
        tftype: Literal["bell", "lowshelf", "highshelf"] | int | None = None,
        auto: Literal["disabled", "off", "on", "adaptive"] | int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "Stream":
        """Apply Dynamic Equalization of input audio.

        Args:
            threshold (float): set detection threshold (from 0 to 100)

                Defaults to 0.
            dfrequency (float): set detection frequency (from 2 to 1e+06)

                Defaults to 1000.
            dqfactor (float): set detection Q factor (from 0.001 to 1000)

                Defaults to 1.
            tfrequency (float): set target frequency (from 2 to 1e+06)

                Defaults to 1000.
            tqfactor (float): set target Q factor (from 0.001 to 1000)

                Defaults to 1.
            attack (float): set detection attack duration (from 0.01 to 2000)

                Defaults to 20.
            release (float): set detection release duration (from 0.01 to 2000)

                Defaults to 200.
            ratio (float): set ratio factor (from 0 to 30)

                Defaults to 1.
            makeup (float): set makeup gain (from 0 to 1000)

                Defaults to 0.
            range (float): set max gain (from 1 to 2000)

                Defaults to 50.
            mode (int | str): set mode (from -1 to 3)

                Allowed values:
                    * listen
                    * cutbelow
                    * cutabove
                    * boostbelow
                    * boostabove

                Defaults to cutbelow.
            dftype (int | str): set detection filter type (from 0 to 3)

                Allowed values:
                    * bandpass
                    * lowpass
                    * highpass
                    * peak

                Defaults to bandpass.
            tftype (int | str): set target filter type (from 0 to 2)

                Allowed values:
                    * bell
                    * lowshelf
                    * highshelf

                Defaults to bell.
            auto (int | str): set auto threshold (from 1 to 4)

                Allowed values:
                    * disabled
                    * off
                    * on
                    * adaptive

                Defaults to off.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adynamicequalizer",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "dfrequency": dfrequency,
                "dqfactor": dqfactor,
                "tfrequency": tfrequency,
                "tqfactor": tqfactor,
                "attack": attack,
                "release": release,
                "ratio": ratio,
                "makeup": makeup,
                "range": range,
                "mode": mode,
                "dftype": dftype,
                "tftype": tftype,
                "auto": auto,
                "precision": precision,
            },
        )[0]

    def adynamicsmooth(
        self, sensitivity: float | None = None, basefreq: float | None = None
    ) -> "Stream":
        """Apply Dynamic Smoothing of input audio.

        Args:
            sensitivity (float): set smooth sensitivity (from 0 to 1e+06)

                Defaults to 2.
            basefreq (float): set base frequency (from 2 to 1e+06)

                Defaults to 22050.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="adynamicsmooth",
            inputs=[self],
            named_arguments={
                "sensitivity": sensitivity,
                "basefreq": basefreq,
            },
        )[0]

    def aecho(
        self,
        in_gain: float | None = None,
        out_gain: float | None = None,
        delays: str | None = None,
        decays: str | None = None,
    ) -> "Stream":
        """Add echoing to the audio.

        Args:
            in_gain (float): set signal input gain (from 0 to 1)

                Defaults to 0.6.
            out_gain (float): set signal output gain (from 0 to 1)

                Defaults to 0.3.
            delays (str): set list of signal delays

                Defaults to 1000.
            decays (str): set list of signal decays

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aecho",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
            },
        )[0]

    def aemphasis(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        mode: Literal["reproduction", "production"] | int | None = None,
        type: Literal["col", "emi", "bsi", "riaa", "cd", "50fm", "75fm", "50kf", "75kf"]
        | int
        | None = None,
    ) -> "Stream":
        """Audio emphasis.

        Args:
            level_in (float): set input gain (from 0 to 64)

                Defaults to 1.
            level_out (float): set output gain (from 0 to 64)

                Defaults to 1.
            mode (int | str): set filter mode (from 0 to 1)

                Allowed values:
                    * reproduction
                    * production

                Defaults to reproduction.
            type (int | str): set filter type (from 0 to 8)

                Allowed values:
                    * col: Columbia
                    * emi: EMI
                    * bsi: BSI (78RPM)
                    * riaa: RIAA
                    * cd: Compact Disc (CD)
                    * 50fm: 50µs (FM)
                    * 75fm: 75µs (FM)
                    * 50kf: 50µs (FM-KF)
                    * 75kf: 75µs (FM-KF)

                Defaults to cd.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aemphasis",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "type": type,
            },
        )[0]

    def aeval(
        self,
        exprs: str | None = None,
        channel_layout: str | None = None,
        c: str | None = None,
    ) -> "Stream":
        """Filter audio signal according to a specified expression.

        Args:
            exprs (str): set the '|'-separated list of channels expressions

            channel_layout (str): set channel layout

            c (str): set channel layout


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aeval",
            inputs=[self],
            named_arguments={
                "exprs": exprs,
                "channel_layout": channel_layout,
                "c": c,
            },
        )[0]

    def aexciter(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        amount: float | None = None,
        drive: float | None = None,
        blend: float | None = None,
        freq: float | None = None,
        ceil: float | None = None,
        listen: bool | None = None,
    ) -> "Stream":
        """Enhance high frequency part of audio.

        Args:
            level_in (float): set level in (from 0 to 64)

                Defaults to 1.
            level_out (float): set level out (from 0 to 64)

                Defaults to 1.
            amount (float): set amount (from 0 to 64)

                Defaults to 1.
            drive (float): set harmonics (from 0.1 to 10)

                Defaults to 8.5.
            blend (float): set blend harmonics (from -10 to 10)

                Defaults to 0.
            freq (float): set scope (from 2000 to 12000)

                Defaults to 7500.
            ceil (float): set ceiling (from 9999 to 20000)

                Defaults to 9999.
            listen (bool): enable listen mode

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aexciter",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "amount": amount,
                "drive": drive,
                "blend": blend,
                "freq": freq,
                "ceil": ceil,
                "listen": listen,
            },
        )[0]

    def afade(
        self,
        type: Literal["in", "out"] | int | None = None,
        t: Literal["in", "out"] | int | None = None,
        start_sample: str | None = None,
        ss: str | None = None,
        nb_samples: str | None = None,
        ns: str | None = None,
        start_time: str | None = None,
        st: str | None = None,
        duration: str | None = None,
        d: str | None = None,
        curve: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
        c: Literal[
            "nofade",
            "tri",
            "qsin",
            "esin",
            "hsin",
            "log",
            "ipar",
            "qua",
            "cub",
            "squ",
            "cbr",
            "par",
            "exp",
            "iqsin",
            "ihsin",
            "dese",
            "desi",
            "losi",
            "sinc",
            "isinc",
            "quat",
            "quatr",
            "qsin2",
            "hsin2",
        ]
        | int
        | None = None,
        silence: float | None = None,
        unity: float | None = None,
    ) -> "Stream":
        """Fade in/out input audio.

        Args:
            type (int | str): set the fade direction (from 0 to 1)

                Allowed values:
                    * in: fade-in
                    * out: fade-out

                Defaults to in.
            t (int | str): set the fade direction (from 0 to 1)

                Allowed values:
                    * in: fade-in
                    * out: fade-out

                Defaults to in.
            start_sample (str): set number of first sample to start fading (from 0 to I64_MAX)

                Defaults to 0.
            ss (str): set number of first sample to start fading (from 0 to I64_MAX)

                Defaults to 0.
            nb_samples (str): set number of samples for fade duration (from 1 to I64_MAX)

                Defaults to 44100.
            ns (str): set number of samples for fade duration (from 1 to I64_MAX)

                Defaults to 44100.
            start_time (str): set time to start fading

                Defaults to 0.
            st (str): set time to start fading

                Defaults to 0.
            duration (str): set fade duration

                Defaults to 0.
            d (str): set fade duration

                Defaults to 0.
            curve (int | str): set fade curve type (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.
            c (int | str): set fade curve type (from -1 to 22)

                Allowed values:
                    * nofade: no fade; keep audio as-is
                    * tri: linear slope
                    * qsin: quarter of sine wave
                    * esin: exponential sine wave
                    * hsin: half of sine wave
                    * log: logarithmic
                    * ipar: inverted parabola
                    * qua: quadratic
                    * cub: cubic
                    * squ: square root
                    * cbr: cubic root
                    * par: parabola
                    * exp: exponential
                    * iqsin: inverted quarter of sine wave
                    * ihsin: inverted half of sine wave
                    * dese: double-exponential seat
                    * desi: double-exponential sigmoid
                    * losi: logistic sigmoid
                    * sinc: sine cardinal function
                    * isinc: inverted sine cardinal function
                    * quat: quartic
                    * quatr: quartic root
                    * qsin2: squared quarter of sine wave
                    * hsin2: squared half of sine wave

                Defaults to tri.
            silence (float): set the silence gain (from 0 to 1)

                Defaults to 0.
            unity (float): set the unity gain (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afade",
            inputs=[self],
            named_arguments={
                "type": type,
                "t": t,
                "start_sample": start_sample,
                "ss": ss,
                "nb_samples": nb_samples,
                "ns": ns,
                "start_time": start_time,
                "st": st,
                "duration": duration,
                "d": d,
                "curve": curve,
                "c": c,
                "silence": silence,
                "unity": unity,
            },
        )[0]

    def afftdn(
        self,
        noise_reduction: float | None = None,
        nr: float | None = None,
        noise_floor: float | None = None,
        nf: float | None = None,
        noise_type: Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | int
        | None = None,
        nt: Literal["white", "w", "vinyl", "v", "shellac", "s", "custom", "c"]
        | int
        | None = None,
        band_noise: str | None = None,
        bn: str | None = None,
        residual_floor: float | None = None,
        rf: float | None = None,
        track_noise: bool | None = None,
        tn: bool | None = None,
        track_residual: bool | None = None,
        tr: bool | None = None,
        output_mode: Literal["input", "i", "output", "o", "noise", "n"]
        | int
        | None = None,
        om: Literal["input", "i", "output", "o", "noise", "n"] | int | None = None,
        adaptivity: float | None = None,
        ad: float | None = None,
        floor_offset: float | None = None,
        fo: float | None = None,
        noise_link: Literal["none", "min", "max", "average"] | int | None = None,
        nl: Literal["none", "min", "max", "average"] | int | None = None,
        band_multiplier: float | None = None,
        bm: float | None = None,
        sample_noise: Literal["none", "start", "begin", "stop", "end"]
        | int
        | None = None,
        sn: Literal["none", "start", "begin", "stop", "end"] | int | None = None,
        gain_smooth: int | None = None,
        gs: int | None = None,
    ) -> "Stream":
        """Denoise audio samples using FFT.

        Args:
            noise_reduction (float): set the noise reduction (from 0.01 to 97)

                Defaults to 12.
            nr (float): set the noise reduction (from 0.01 to 97)

                Defaults to 12.
            noise_floor (float): set the noise floor (from -80 to -20)

                Defaults to -50.
            nf (float): set the noise floor (from -80 to -20)

                Defaults to -50.
            noise_type (int | str): set the noise type (from 0 to 3)

                Allowed values:
                    * white: white noise
                    * w: white noise
                    * vinyl: vinyl noise
                    * v: vinyl noise
                    * shellac: shellac noise
                    * s: shellac noise
                    * custom: custom noise
                    * c: custom noise

                Defaults to white.
            nt (int | str): set the noise type (from 0 to 3)

                Allowed values:
                    * white: white noise
                    * w: white noise
                    * vinyl: vinyl noise
                    * v: vinyl noise
                    * shellac: shellac noise
                    * s: shellac noise
                    * custom: custom noise
                    * c: custom noise

                Defaults to white.
            band_noise (str): set the custom bands noise

            bn (str): set the custom bands noise

            residual_floor (float): set the residual floor (from -80 to -20)

                Defaults to -38.
            rf (float): set the residual floor (from -80 to -20)

                Defaults to -38.
            track_noise (bool): track noise

                Defaults to false.
            tn (bool): track noise

                Defaults to false.
            track_residual (bool): track residual

                Defaults to false.
            tr (bool): track residual

                Defaults to false.
            output_mode (int | str): set output mode (from 0 to 2)

                Allowed values:
                    * input: input
                    * i: input
                    * output: output
                    * o: output
                    * noise: noise
                    * n: noise

                Defaults to output.
            om (int | str): set output mode (from 0 to 2)

                Allowed values:
                    * input: input
                    * i: input
                    * output: output
                    * o: output
                    * noise: noise
                    * n: noise

                Defaults to output.
            adaptivity (float): set adaptivity factor (from 0 to 1)

                Defaults to 0.5.
            ad (float): set adaptivity factor (from 0 to 1)

                Defaults to 0.5.
            floor_offset (float): set noise floor offset factor (from -2 to 2)

                Defaults to 1.
            fo (float): set noise floor offset factor (from -2 to 2)

                Defaults to 1.
            noise_link (int | str): set the noise floor link (from 0 to 3)

                Allowed values:
                    * none: none
                    * min: min
                    * max: max
                    * average: average

                Defaults to min.
            nl (int | str): set the noise floor link (from 0 to 3)

                Allowed values:
                    * none: none
                    * min: min
                    * max: max
                    * average: average

                Defaults to min.
            band_multiplier (float): set band multiplier (from 0.2 to 5)

                Defaults to 1.25.
            bm (float): set band multiplier (from 0.2 to 5)

                Defaults to 1.25.
            sample_noise (int | str): set sample noise mode (from 0 to 2)

                Allowed values:
                    * none: none
                    * start: start
                    * begin: start
                    * stop: stop
                    * end: stop

                Defaults to none.
            sn (int | str): set sample noise mode (from 0 to 2)

                Allowed values:
                    * none: none
                    * start: start
                    * begin: start
                    * stop: stop
                    * end: stop

                Defaults to none.
            gain_smooth (int): set gain smooth radius (from 0 to 50)

                Defaults to 0.
            gs (int): set gain smooth radius (from 0 to 50)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afftdn",
            inputs=[self],
            named_arguments={
                "noise_reduction": noise_reduction,
                "nr": nr,
                "noise_floor": noise_floor,
                "nf": nf,
                "noise_type": noise_type,
                "nt": nt,
                "band_noise": band_noise,
                "bn": bn,
                "residual_floor": residual_floor,
                "rf": rf,
                "track_noise": track_noise,
                "tn": tn,
                "track_residual": track_residual,
                "tr": tr,
                "output_mode": output_mode,
                "om": om,
                "adaptivity": adaptivity,
                "ad": ad,
                "floor_offset": floor_offset,
                "fo": fo,
                "noise_link": noise_link,
                "nl": nl,
                "band_multiplier": band_multiplier,
                "bm": bm,
                "sample_noise": sample_noise,
                "sn": sn,
                "gain_smooth": gain_smooth,
                "gs": gs,
            },
        )[0]

    def afftfilt(
        self,
        real: str | None = None,
        imag: str | None = None,
        win_size: int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        overlap: float | None = None,
    ) -> "Stream":
        """Apply arbitrary expressions to samples in frequency domain.

        Args:
            real (str): set channels real expressions

                Defaults to re.
            imag (str): set channels imaginary expressions

                Defaults to im.
            win_size (int): set window size (from 16 to 131072)

                Defaults to 4096.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 0.75.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afftfilt",
            inputs=[self],
            named_arguments={
                "real": real,
                "imag": imag,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            },
        )[0]

    def afir(
        self,
        *streams: "Stream",
        dry: float | None = None,
        wet: float | None = None,
        length: float | None = None,
        gtype: Literal["none", "peak", "dc", "gn", "ac", "rms"] | int | None = None,
        irnorm: float | None = None,
        irlink: bool | None = None,
        irgain: float | None = None,
        irfmt: Literal["mono", "input"] | int | None = None,
        maxir: float | None = None,
        response: bool | None = None,
        channel: int | None = None,
        size: str | None = None,
        rate: str | None = None,
        minp: int | None = None,
        maxp: int | None = None,
        nbirs: int | None = None,
        ir: int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
        irload: Literal["init", "access"] | int | None = None,
    ) -> "Stream":
        """Apply Finite Impulse Response filter with supplied coefficients in additional stream(s).

        Args:
            *streams (Stream): One or more input streams.
            dry (float): set dry gain (from 0 to 10)

                Defaults to 1.
            wet (float): set wet gain (from 0 to 10)

                Defaults to 1.
            length (float): set IR length (from 0 to 1)

                Defaults to 1.
            gtype (int | str): set IR auto gain type (from -1 to 4)

                Allowed values:
                    * none: without auto gain
                    * peak: peak gain
                    * dc: DC gain
                    * gn: gain to noise
                    * ac: AC gain
                    * rms: RMS gain

                Defaults to peak.
            irnorm (float): set IR norm (from -1 to 2)

                Defaults to 1.
            irlink (bool): set IR link

                Defaults to true.
            irgain (float): set IR gain (from 0 to 1)

                Defaults to 1.
            irfmt (int | str): set IR format (from 0 to 1)

                Allowed values:
                    * mono: single channel
                    * input: same as input

                Defaults to input.
            maxir (float): set max IR length (from 0.1 to 60)

                Defaults to 30.
            response (bool): show IR frequency response

                Defaults to false.
            channel (int): set IR channel to display frequency response (from 0 to 1024)

                Defaults to 0.
            size (str): set video size

                Defaults to hd720.
            rate (str): set video rate

                Defaults to 25.
            minp (int): set min partition size (from 1 to 65536)

                Defaults to 8192.
            maxp (int): set max partition size (from 8 to 65536)

                Defaults to 8192.
            nbirs (int): set number of input IRs (from 1 to 32)

                Defaults to 1.
            ir (int): select IR (from 0 to 31)

                Defaults to 0.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.
            irload (int | str): set IR loading type (from 0 to 1)

                Allowed values:
                    * init: load all IRs on init
                    * access: load IR on access

                Defaults to init.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afir",
            inputs=[self, *streams],
            named_arguments={
                "dry": dry,
                "wet": wet,
                "length": length,
                "gtype": gtype,
                "irnorm": irnorm,
                "irlink": irlink,
                "irgain": irgain,
                "irfmt": irfmt,
                "maxir": maxir,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
                "minp": minp,
                "maxp": maxp,
                "nbirs": nbirs,
                "ir": ir,
                "precision": precision,
                "irload": irload,
            },
        )[0]

    def aformat(
        self,
    ) -> "Stream":
        """Convert the input audio to one of the specified formats.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aformat", inputs=[self], named_arguments={}
        )[0]

    def afreqshift(
        self,
        shift: float | None = None,
        level: float | None = None,
        order: int | None = None,
    ) -> "Stream":
        """Apply frequency shifting to input audio.

        Args:
            shift (float): set frequency shift (from -2.14748e+09 to INT_MAX)

                Defaults to 0.
            level (float): set output level (from 0 to 1)

                Defaults to 1.
            order (int): set filter order (from 1 to 16)

                Defaults to 8.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afreqshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "level": level,
                "order": order,
            },
        )[0]

    def afwtdn(
        self,
        sigma: float | None = None,
        levels: int | None = None,
        wavet: Literal["sym2", "sym4", "rbior68", "deb10", "sym10", "coif5", "bl3"]
        | int
        | None = None,
        percent: float | None = None,
        profile: bool | None = None,
        adaptive: bool | None = None,
        samples: int | None = None,
        softness: float | None = None,
    ) -> "Stream":
        """Denoise audio stream using Wavelets.

        Args:
            sigma (float): set noise sigma (from 0 to 1)

                Defaults to 0.
            levels (int): set number of wavelet levels (from 1 to 12)

                Defaults to 10.
            wavet (int | str): set wavelet type (from 0 to 6)

                Allowed values:
                    * sym2: sym2
                    * sym4: sym4
                    * rbior68: rbior68
                    * deb10: deb10
                    * sym10: sym10
                    * coif5: coif5
                    * bl3: bl3

                Defaults to sym10.
            percent (float): set percent of full denoising (from 0 to 100)

                Defaults to 85.
            profile (bool): profile noise

                Defaults to false.
            adaptive (bool): adaptive profiling of noise

                Defaults to false.
            samples (int): set frame size in number of samples (from 512 to 65536)

                Defaults to 8192.
            softness (float): set thresholding softness (from 0 to 10)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="afwtdn",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "levels": levels,
                "wavet": wavet,
                "percent": percent,
                "profile": profile,
                "adaptive": adaptive,
                "samples": samples,
                "softness": softness,
            },
        )[0]

    def agate(
        self,
        level_in: float | None = None,
        mode: Literal["downward", "upward"] | int | None = None,
        range: float | None = None,
        threshold: float | None = None,
        ratio: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        makeup: float | None = None,
        knee: float | None = None,
        detection: Literal["peak", "rms"] | int | None = None,
        link: Literal["average", "maximum"] | int | None = None,
        level_sc: float | None = None,
    ) -> "Stream":
        """Audio gate.

        Args:
            level_in (float): set input level (from 0.015625 to 64)

                Defaults to 1.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * downward
                    * upward

                Defaults to downward.
            range (float): set max gain reduction (from 0 to 1)

                Defaults to 0.06125.
            threshold (float): set threshold (from 0 to 1)

                Defaults to 0.125.
            ratio (float): set ratio (from 1 to 9000)

                Defaults to 2.
            attack (float): set attack (from 0.01 to 9000)

                Defaults to 20.
            release (float): set release (from 0.01 to 9000)

                Defaults to 250.
            makeup (float): set makeup gain (from 1 to 64)

                Defaults to 1.
            knee (float): set knee (from 1 to 8)

                Defaults to 2.82843.
            detection (int | str): set detection (from 0 to 1)

                Allowed values:
                    * peak
                    * rms

                Defaults to rms.
            link (int | str): set link (from 0 to 1)

                Allowed values:
                    * average
                    * maximum

                Defaults to average.
            level_sc (float): set sidechain gain (from 0.015625 to 64)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="agate",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "range": range,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "detection": detection,
                "link": link,
                "level_sc": level_sc,
            },
        )[0]

    def agraphmonitor(
        self,
        size: str | None = None,
        s: str | None = None,
        opacity: float | None = None,
        o: float | None = None,
        mode: Literal["full", "compact", "nozero", "noeof", "nodisabled"] | None = None,
        m: Literal["full", "compact", "nozero", "noeof", "nodisabled"] | None = None,
        flags: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ]
        | None = None,
        f: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ]
        | None = None,
        rate: str | None = None,
        r: str | None = None,
    ) -> "Stream":
        """Show various filtergraph stats.

        Args:
            size (str): set monitor size

                Defaults to hd720.
            s (str): set monitor size

                Defaults to hd720.
            opacity (float): set video opacity (from 0 to 1)

                Defaults to 0.9.
            o (float): set video opacity (from 0 to 1)

                Defaults to 0.9.
            mode (str): set mode

                Allowed values:
                    * full
                    * compact
                    * nozero
                    * noeof
                    * nodisabled

                Defaults to 0.
            m (str): set mode

                Allowed values:
                    * full
                    * compact
                    * nozero
                    * noeof
                    * nodisabled

                Defaults to 0.
            flags (str): set flags

                Allowed values:
                    * none
                    * all
                    * queue
                    * frame_count_in
                    * frame_count_out
                    * frame_count_delta
                    * pts
                    * pts_delta
                    * time
                    * time_delta
                    * timebase
                    * format
                    * size
                    * rate
                    * eof
                    * sample_count_in
                    * sample_count_out
                    * sample_count_delta
                    * disabled

                Defaults to all+queue.
            f (str): set flags

                Allowed values:
                    * none
                    * all
                    * queue
                    * frame_count_in
                    * frame_count_out
                    * frame_count_delta
                    * pts
                    * pts_delta
                    * time
                    * time_delta
                    * timebase
                    * format
                    * size
                    * rate
                    * eof
                    * sample_count_in
                    * sample_count_out
                    * sample_count_delta
                    * disabled

                Defaults to all+queue.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="agraphmonitor",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "opacity": opacity,
                "o": o,
                "mode": mode,
                "m": m,
                "flags": flags,
                "f": f,
                "rate": rate,
                "r": r,
            },
        )[0]

    def ahistogram(
        self,
        dmode: Literal["single", "separate"] | int | None = None,
        rate: str | None = None,
        r: str | None = None,
        size: str | None = None,
        s: str | None = None,
        scale: Literal["log", "sqrt", "cbrt", "lin", "rlog"] | int | None = None,
        ascale: Literal["log", "lin"] | int | None = None,
        acount: int | None = None,
        rheight: float | None = None,
        slide: Literal["replace", "scroll"] | int | None = None,
        hmode: Literal["abs", "sign"] | int | None = None,
    ) -> "Stream":
        """Convert input audio to histogram video output.

        Args:
            dmode (int | str): set method to display channels (from 0 to 1)

                Allowed values:
                    * single: all channels use single histogram
                    * separate: each channel have own histogram

                Defaults to single.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            size (str): set video size

                Defaults to hd720.
            s (str): set video size

                Defaults to hd720.
            scale (int | str): set display scale (from 0 to 4)

                Allowed values:
                    * log: logarithmic
                    * sqrt: square root
                    * cbrt: cubic root
                    * lin: linear
                    * rlog: reverse logarithmic

                Defaults to log.
            ascale (int | str): set amplitude scale (from 0 to 1)

                Allowed values:
                    * log: logarithmic
                    * lin: linear

                Defaults to log.
            acount (int): how much frames to accumulate (from -1 to 100)

                Defaults to 1.
            rheight (float): set histogram ratio of window height (from 0 to 1)

                Defaults to 0.1.
            slide (int | str): set sonogram sliding (from 0 to 1)

                Allowed values:
                    * replace: replace old rows with new
                    * scroll: scroll from top to bottom

                Defaults to replace.
            hmode (int | str): set histograms mode (from 0 to 1)

                Allowed values:
                    * abs: use absolute samples
                    * sign: use unchanged samples

                Defaults to abs.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ahistogram",
            inputs=[self],
            named_arguments={
                "dmode": dmode,
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "scale": scale,
                "ascale": ascale,
                "acount": acount,
                "rheight": rheight,
                "slide": slide,
                "hmode": hmode,
            },
        )[0]

    def aiir(
        self,
        zeros: str | None = None,
        z: str | None = None,
        poles: str | None = None,
        p: str | None = None,
        gains: str | None = None,
        k: str | None = None,
        dry: float | None = None,
        wet: float | None = None,
        format: Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | int | None = None,
        f: Literal["ll", "sf", "tf", "zp", "pr", "pd", "sp"] | int | None = None,
        process: Literal["d", "s", "p"] | int | None = None,
        r: Literal["d", "s", "p"] | int | None = None,
        precision: Literal["dbl", "flt", "i32", "i16"] | int | None = None,
        e: Literal["dbl", "flt", "i32", "i16"] | int | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        mix: float | None = None,
        response: bool | None = None,
        channel: int | None = None,
        size: str | None = None,
        rate: str | None = None,
    ) -> "FilterMultiOutput":
        """Apply Infinite Impulse Response filter with supplied coefficients.

        Args:
            zeros (str): set B/numerator/zeros/reflection coefficients

                Defaults to 1+0i 1-0i.
            z (str): set B/numerator/zeros/reflection coefficients

                Defaults to 1+0i 1-0i.
            poles (str): set A/denominator/poles/ladder coefficients

                Defaults to 1+0i 1-0i.
            p (str): set A/denominator/poles/ladder coefficients

                Defaults to 1+0i 1-0i.
            gains (str): set channels gains

                Defaults to 1|1.
            k (str): set channels gains

                Defaults to 1|1.
            dry (float): set dry gain (from 0 to 1)

                Defaults to 1.
            wet (float): set wet gain (from 0 to 1)

                Defaults to 1.
            format (int | str): set coefficients format (from -2 to 4)

                Allowed values:
                    * ll: lattice-ladder function
                    * sf: analog transfer function
                    * tf: digital transfer function
                    * zp: Z-plane zeros/poles
                    * pr: Z-plane zeros/poles (polar radians)
                    * pd: Z-plane zeros/poles (polar degrees)
                    * sp: S-plane zeros/poles

                Defaults to zp.
            f (int | str): set coefficients format (from -2 to 4)

                Allowed values:
                    * ll: lattice-ladder function
                    * sf: analog transfer function
                    * tf: digital transfer function
                    * zp: Z-plane zeros/poles
                    * pr: Z-plane zeros/poles (polar radians)
                    * pd: Z-plane zeros/poles (polar degrees)
                    * sp: S-plane zeros/poles

                Defaults to zp.
            process (int | str): set kind of processing (from 0 to 2)

                Allowed values:
                    * d: direct
                    * s: serial
                    * p: parallel

                Defaults to s.
            r (int | str): set kind of processing (from 0 to 2)

                Allowed values:
                    * d: direct
                    * s: serial
                    * p: parallel

                Defaults to s.
            precision (int | str): set filtering precision (from 0 to 3)

                Allowed values:
                    * dbl: double-precision floating-point
                    * flt: single-precision floating-point
                    * i32: 32-bit integers
                    * i16: 16-bit integers

                Defaults to dbl.
            e (int | str): set precision (from 0 to 3)

                Allowed values:
                    * dbl: double-precision floating-point
                    * flt: single-precision floating-point
                    * i32: 32-bit integers
                    * i16: 16-bit integers

                Defaults to dbl.
            normalize (bool): normalize coefficients

                Defaults to true.
            n (bool): normalize coefficients

                Defaults to true.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            response (bool): show IR frequency response

                Defaults to false.
            channel (int): set IR channel to display frequency response (from 0 to 1024)

                Defaults to 0.
            size (str): set video size

                Defaults to hd720.
            rate (str): set video rate

                Defaults to 25.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="aiir",
            inputs=[self],
            named_arguments={
                "zeros": zeros,
                "z": z,
                "poles": poles,
                "p": p,
                "gains": gains,
                "k": k,
                "dry": dry,
                "wet": wet,
                "format": format,
                "f": f,
                "process": process,
                "r": r,
                "precision": precision,
                "e": e,
                "normalize": normalize,
                "n": n,
                "mix": mix,
                "response": response,
                "channel": channel,
                "size": size,
                "rate": rate,
            },
        )

    def aintegral(
        self,
    ) -> "Stream":
        """Compute integral of input audio.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aintegral", inputs=[self], named_arguments={}
        )[0]

    def ainterleave(
        self,
        *streams: "Stream",
        nb_inputs: int | None = None,
        n: int | None = None,
        duration: Literal["longest", "shortest", "first"] | int | None = None,
    ) -> "Stream":
        """Temporally interleave audio inputs.

        Args:
            *streams (Stream): One or more input streams.
            nb_inputs (int): set number of inputs (from 1 to INT_MAX)

                Defaults to 2.
            n (int): set number of inputs (from 1 to INT_MAX)

                Defaults to 2.
            duration (int | str): how to determine the end-of-stream (from 0 to 2)

                Allowed values:
                    * longest: Duration of longest input
                    * shortest: Duration of shortest input
                    * first: Duration of first input

                Defaults to longest.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ainterleave",
            inputs=[self, *streams],
            named_arguments={
                "nb_inputs": nb_inputs,
                "n": n,
                "duration": duration,
            },
        )[0]

    def alatency(
        self,
    ) -> "Stream":
        """Report audio filtering latency.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="alatency", inputs=[self], named_arguments={}
        )[0]

    def alimiter(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        limit: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        asc: bool | None = None,
        asc_level: float | None = None,
        level: bool | None = None,
        latency: bool | None = None,
    ) -> "Stream":
        """Audio lookahead limiter.

        Args:
            level_in (float): set input level (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set output level (from 0.015625 to 64)

                Defaults to 1.
            limit (float): set limit (from 0.0625 to 1)

                Defaults to 1.
            attack (float): set attack (from 0.1 to 80)

                Defaults to 5.
            release (float): set release (from 1 to 8000)

                Defaults to 50.
            asc (bool): enable asc

                Defaults to false.
            asc_level (float): set asc level (from 0 to 1)

                Defaults to 0.5.
            level (bool): auto level

                Defaults to true.
            latency (bool): compensate delay

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="alimiter",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "limit": limit,
                "attack": attack,
                "release": release,
                "asc": asc,
                "asc_level": asc_level,
                "level": level,
                "latency": latency,
            },
        )[0]

    def allpass(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        order: int | None = None,
        o: int | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
    ) -> "Stream":
        """Apply a two-pole all-pass filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.707.
            w (float): set width (from 0 to 99999)

                Defaults to 0.707.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            order (int): set filter order (from 1 to 2)

                Defaults to 2.
            o (int): set filter order (from 1 to 2)

                Defaults to 2.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="allpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "order": order,
                "o": o,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
            },
        )[0]

    def aloop(
        self,
        loop: int | None = None,
        size: str | None = None,
        start: str | None = None,
        time: str | None = None,
    ) -> "Stream":
        """Loop audio samples.

        Args:
            loop (int): number of loops (from -1 to INT_MAX)

                Defaults to 0.
            size (str): max number of samples to loop (from 0 to INT_MAX)

                Defaults to 0.
            start (str): set the loop start sample (from -1 to I64_MAX)

                Defaults to 0.
            time (str): set the loop start time

                Defaults to INT64_MAX.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aloop",
            inputs=[self],
            named_arguments={
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            },
        )[0]

    def alphaextract(
        self,
    ) -> "Stream":
        """Extract an alpha channel as a grayscale image component.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="alphaextract", inputs=[self], named_arguments={}
        )[0]

    def alphamerge(self, alpha_stream: "Stream") -> "Stream":
        """Copy the luma value of the second input into the alpha channel of the first input.

        Args:
            alpha_stream (Stream): Input video stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="alphamerge", inputs=[self, alpha_stream], named_arguments={}
        )[0]

    def amerge(self, *streams: "Stream", inputs: int | None = None) -> "Stream":
        """Merge two or more audio streams into a single multi-channel stream.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): specify the number of inputs (from 1 to 64)

                Defaults to 2.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="amerge",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
            },
        )[0]

    def ametadata(
        self,
        mode: Literal["select", "add", "modify", "delete", "print"] | int | None = None,
        key: str | None = None,
        value: str | None = None,
        function: Literal[
            "same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"
        ]
        | int
        | None = None,
        expr: str | None = None,
        file: str | None = None,
        direct: bool | None = None,
    ) -> "Stream":
        """Manipulate audio frame metadata.

        Args:
            mode (int | str): set a mode of operation (from 0 to 4)

                Allowed values:
                    * select: select frame
                    * add: add new metadata
                    * modify: modify metadata
                    * delete: delete metadata
                    * print: print metadata

                Defaults to select.
            key (str): set metadata key

            value (str): set metadata value

            function (int | str): function for comparing values (from 0 to 6)

                Allowed values:
                    * same_str
                    * starts_with
                    * less
                    * equal
                    * greater
                    * expr
                    * ends_with

                Defaults to same_str.
            expr (str): set expression for expr function

            file (str): set file where to print metadata information

            direct (bool): reduce buffering when printing to user-set file or pipe

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ametadata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
            },
        )[0]

    def amix(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        duration: Literal["longest", "shortest", "first"] | int | None = None,
        dropout_transition: float | None = None,
        weights: str | None = None,
        normalize: bool | None = None,
    ) -> "Stream":
        """Audio mixing.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): Number of inputs. (from 1 to 32767)

                Defaults to 2.
            duration (int | str): How to determine the end-of-stream. (from 0 to 2)

                Allowed values:
                    * longest: Duration of longest input.
                    * shortest: Duration of shortest input.
                    * first: Duration of first input.

                Defaults to longest.
            dropout_transition (float): Transition time, in seconds, for volume renormalization when an input stream ends. (from 0 to INT_MAX)

                Defaults to 2.
            weights (str): Set weight for each input.

                Defaults to 1 1.
            normalize (bool): Scale inputs

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="amix",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "duration": duration,
                "dropout_transition": dropout_transition,
                "weights": weights,
                "normalize": normalize,
            },
        )[0]

    def amplify(
        self,
        radius: int | None = None,
        factor: float | None = None,
        threshold: float | None = None,
        tolerance: float | None = None,
        low: float | None = None,
        high: float | None = None,
        planes: str | None = None,
    ) -> "Stream":
        """Amplify changes between successive video frames.

        Args:
            radius (int): set radius (from 1 to 63)

                Defaults to 2.
            factor (float): set factor (from 0 to 65535)

                Defaults to 2.
            threshold (float): set threshold (from 0 to 65535)

                Defaults to 10.
            tolerance (float): set tolerance (from 0 to 65535)

                Defaults to 0.
            low (float): set low limit for amplification (from 0 to 65535)

                Defaults to 65535.
            high (float): set high limit for amplification (from 0 to 65535)

                Defaults to 65535.
            planes (str): set what planes to filter

                Defaults to 7.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="amplify",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "factor": factor,
                "threshold": threshold,
                "tolerance": tolerance,
                "low": low,
                "high": high,
                "planes": planes,
            },
        )[0]

    def amultiply(self, multiply1_stream: "Stream") -> "Stream":
        """Multiply two audio streams.

        Args:
            multiply1_stream (Stream): Input audio stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="amultiply", inputs=[self, multiply1_stream], named_arguments={}
        )[0]

    def anequalizer(
        self,
        params: str | None = None,
        curves: bool | None = None,
        size: str | None = None,
        mgain: float | None = None,
        fscale: Literal["lin", "log"] | int | None = None,
        colors: str | None = None,
    ) -> "FilterMultiOutput":
        """Apply high-order audio parametric multi band equalizer.

        Args:
            params (str): No description available.

            curves (bool): draw frequency response curves

                Defaults to false.
            size (str): set video size

                Defaults to hd720.
            mgain (float): set max gain (from -900 to 900)

                Defaults to 60.
            fscale (int | str): set frequency scale (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: logarithmic

                Defaults to log.
            colors (str): set channels curves colors

                Defaults to red|green|blue|yellow|orange|lime|pink|magenta|brown.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="anequalizer",
            inputs=[self],
            named_arguments={
                "params": params,
                "curves": curves,
                "size": size,
                "mgain": mgain,
                "fscale": fscale,
                "colors": colors,
            },
        )

    def anlmdn(
        self,
        strength: float | None = None,
        s: float | None = None,
        patch: str | None = None,
        p: str | None = None,
        research: str | None = None,
        r: str | None = None,
        output: Literal["i", "o", "n"] | int | None = None,
        o: Literal["i", "o", "n"] | int | None = None,
        smooth: float | None = None,
        m: float | None = None,
    ) -> "Stream":
        """Reduce broadband noise from stream using Non-Local Means.

        Args:
            strength (float): set denoising strength (from 1e-05 to 10000)

                Defaults to 1e-05.
            s (float): set denoising strength (from 1e-05 to 10000)

                Defaults to 1e-05.
            patch (str): set patch duration

                Defaults to 0.002.
            p (str): set patch duration

                Defaults to 0.002.
            research (str): set research duration

                Defaults to 0.006.
            r (str): set research duration

                Defaults to 0.006.
            output (int | str): set output mode (from 0 to 2)

                Allowed values:
                    * i: input
                    * o: output
                    * n: noise

                Defaults to o.
            o (int | str): set output mode (from 0 to 2)

                Allowed values:
                    * i: input
                    * o: output
                    * n: noise

                Defaults to o.
            smooth (float): set smooth factor (from 1 to 1000)

                Defaults to 11.
            m (float): set smooth factor (from 1 to 1000)

                Defaults to 11.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="anlmdn",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "s": s,
                "patch": patch,
                "p": p,
                "research": research,
                "r": r,
                "output": output,
                "o": o,
                "smooth": smooth,
                "m": m,
            },
        )[0]

    def anlmf(
        self,
        desired_stream: "Stream",
        order: int | None = None,
        mu: float | None = None,
        eps: float | None = None,
        leakage: float | None = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "Stream":
        """Apply Normalized Least-Mean-Fourth algorithm to first audio stream.

        Args:
            desired_stream (Stream): Input audio stream.
            order (int): set the filter order (from 1 to 32767)

                Defaults to 256.
            mu (float): set the filter mu (from 0 to 2)

                Defaults to 0.75.
            eps (float): set the filter eps (from 0 to 1)

                Defaults to 1.
            leakage (float): set the filter leakage (from 0 to 1)

                Defaults to 0.
            out_mode (int | str): set output mode (from 0 to 4)

                Allowed values:
                    * i: input
                    * d: desired
                    * o: output
                    * n: noise
                    * e: error

                Defaults to o.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="anlmf",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def anlms(
        self,
        desired_stream: "Stream",
        order: int | None = None,
        mu: float | None = None,
        eps: float | None = None,
        leakage: float | None = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "Stream":
        """Apply Normalized Least-Mean-Squares algorithm to first audio stream.

        Args:
            desired_stream (Stream): Input audio stream.
            order (int): set the filter order (from 1 to 32767)

                Defaults to 256.
            mu (float): set the filter mu (from 0 to 2)

                Defaults to 0.75.
            eps (float): set the filter eps (from 0 to 1)

                Defaults to 1.
            leakage (float): set the filter leakage (from 0 to 1)

                Defaults to 0.
            out_mode (int | str): set output mode (from 0 to 4)

                Allowed values:
                    * i: input
                    * d: desired
                    * o: output
                    * n: noise
                    * e: error

                Defaults to o.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="anlms",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "mu": mu,
                "eps": eps,
                "leakage": leakage,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def anull(
        self,
    ) -> "Stream":
        """Pass the source unchanged to the output.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="anull", inputs=[self], named_arguments={}
        )[0]

    def anullsink(
        self,
    ) -> "SinkNode":
        """Do absolutely nothing with the input audio.

        Returns:
            "SinkNode": A SinkNode representing the sink (terminal node).
        """
        return self._apply_sink_filter(
            filter_name="anullsink", inputs=[self], named_arguments={}
        )

    def apad(
        self,
        packet_size: int | None = None,
        pad_len: str | None = None,
        whole_len: str | None = None,
        pad_dur: str | None = None,
        whole_dur: str | None = None,
    ) -> "Stream":
        """Pad audio with silence.

        Args:
            packet_size (int): set silence packet size (from 0 to INT_MAX)

                Defaults to 4096.
            pad_len (str): set number of samples of silence to add (from -1 to I64_MAX)

                Defaults to -1.
            whole_len (str): set minimum target number of samples in the audio stream (from -1 to I64_MAX)

                Defaults to -1.
            pad_dur (str): set duration of silence to add

                Defaults to -0.000001.
            whole_dur (str): set minimum target duration in the audio stream

                Defaults to -0.000001.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="apad",
            inputs=[self],
            named_arguments={
                "packet_size": packet_size,
                "pad_len": pad_len,
                "whole_len": whole_len,
                "pad_dur": pad_dur,
                "whole_dur": whole_dur,
            },
        )[0]

    def aperms(
        self,
        mode: Literal["none", "ro", "rw", "toggle", "random"] | int | None = None,
        seed: str | None = None,
    ) -> "Stream":
        """Set permissions for the output audio frame.

        Args:
            mode (int | str): select permissions mode (from 0 to 4)

                Allowed values:
                    * none: do nothing
                    * ro: set all output frames read-only
                    * rw: set all output frames writable
                    * toggle: switch permissions
                    * random: set permissions randomly

                Defaults to none.
            seed (str): set the seed for the random mode (from -1 to UINT32_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aperms",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "seed": seed,
            },
        )[0]

    def aphasemeter(
        self,
        rate: str | None = None,
        r: str | None = None,
        size: str | None = None,
        s: str | None = None,
        rc: int | None = None,
        gc: int | None = None,
        bc: int | None = None,
        mpc: str | None = None,
        video: bool | None = None,
        phasing: bool | None = None,
        tolerance: float | None = None,
        t: float | None = None,
        angle: float | None = None,
        a: float | None = None,
        duration: str | None = None,
        d: str | None = None,
    ) -> "FilterMultiOutput":
        """Convert input audio to phase meter video output.

        Args:
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            size (str): set video size

                Defaults to 800x400.
            s (str): set video size

                Defaults to 800x400.
            rc (int): set red contrast (from 0 to 255)

                Defaults to 2.
            gc (int): set green contrast (from 0 to 255)

                Defaults to 7.
            bc (int): set blue contrast (from 0 to 255)

                Defaults to 1.
            mpc (str): set median phase color

                Defaults to none.
            video (bool): set video output

                Defaults to true.
            phasing (bool): set mono and out-of-phase detection output

                Defaults to false.
            tolerance (float): set phase tolerance for mono detection (from 0 to 1)

                Defaults to 0.
            t (float): set phase tolerance for mono detection (from 0 to 1)

                Defaults to 0.
            angle (float): set angle threshold for out-of-phase detection (from 90 to 180)

                Defaults to 170.
            a (float): set angle threshold for out-of-phase detection (from 90 to 180)

                Defaults to 170.
            duration (str): set minimum mono or out-of-phase duration in seconds

                Defaults to 2.
            d (str): set minimum mono or out-of-phase duration in seconds

                Defaults to 2.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="aphasemeter",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "mpc": mpc,
                "video": video,
                "phasing": phasing,
                "tolerance": tolerance,
                "t": t,
                "angle": angle,
                "a": a,
                "duration": duration,
                "d": d,
            },
        )

    def aphaser(
        self,
        in_gain: float | None = None,
        out_gain: float | None = None,
        delay: float | None = None,
        decay: float | None = None,
        speed: float | None = None,
        type: Literal["triangular", "t", "sinusoidal", "s"] | int | None = None,
    ) -> "Stream":
        """Add a phasing effect to the audio.

        Args:
            in_gain (float): set input gain (from 0 to 1)

                Defaults to 0.4.
            out_gain (float): set output gain (from 0 to 1e+09)

                Defaults to 0.74.
            delay (float): set delay in milliseconds (from 0 to 5)

                Defaults to 3.
            decay (float): set decay (from 0 to 0.99)

                Defaults to 0.4.
            speed (float): set modulation speed (from 0.1 to 2)

                Defaults to 0.5.
            type (int | str): set modulation type (from 0 to 1)

                Allowed values:
                    * triangular
                    * t
                    * sinusoidal
                    * s

                Defaults to triangular.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aphaser",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delay": delay,
                "decay": decay,
                "speed": speed,
                "type": type,
            },
        )[0]

    def aphaseshift(
        self,
        shift: float | None = None,
        level: float | None = None,
        order: int | None = None,
    ) -> "Stream":
        """Apply phase shifting to input audio.

        Args:
            shift (float): set phase shift (from -1 to 1)

                Defaults to 0.
            level (float): set output level (from 0 to 1)

                Defaults to 1.
            order (int): set filter order (from 1 to 16)

                Defaults to 8.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aphaseshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "level": level,
                "order": order,
            },
        )[0]

    def apsnr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Peak Signal-to-Noise Ratio.

        Args:
            input1_stream (Stream): Input audio stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="apsnr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def apsyclip(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        clip: float | None = None,
        diff: bool | None = None,
        adaptive: float | None = None,
        iterations: int | None = None,
        level: bool | None = None,
    ) -> "Stream":
        """Audio Psychoacoustic Clipper.

        Args:
            level_in (float): set input level (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set output level (from 0.015625 to 64)

                Defaults to 1.
            clip (float): set clip level (from 0.015625 to 1)

                Defaults to 1.
            diff (bool): enable difference

                Defaults to false.
            adaptive (float): set adaptive distortion (from 0 to 1)

                Defaults to 0.5.
            iterations (int): set iterations (from 1 to 20)

                Defaults to 10.
            level (bool): set auto level

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="apsyclip",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "clip": clip,
                "diff": diff,
                "adaptive": adaptive,
                "iterations": iterations,
                "level": level,
            },
        )[0]

    def apulsator(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        mode: Literal["sine", "triangle", "square", "sawup", "sawdown"]
        | int
        | None = None,
        amount: float | None = None,
        offset_l: float | None = None,
        offset_r: float | None = None,
        width: float | None = None,
        timing: Literal["bpm", "ms", "hz"] | int | None = None,
        bpm: float | None = None,
        ms: int | None = None,
        hz: float | None = None,
    ) -> "Stream":
        """Audio pulsator.

        Args:
            level_in (float): set input gain (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set output gain (from 0.015625 to 64)

                Defaults to 1.
            mode (int | str): set mode (from 0 to 4)

                Allowed values:
                    * sine
                    * triangle
                    * square
                    * sawup
                    * sawdown

                Defaults to sine.
            amount (float): set modulation (from 0 to 1)

                Defaults to 1.
            offset_l (float): set offset L (from 0 to 1)

                Defaults to 0.
            offset_r (float): set offset R (from 0 to 1)

                Defaults to 0.5.
            width (float): set pulse width (from 0 to 2)

                Defaults to 1.
            timing (int | str): set timing (from 0 to 2)

                Allowed values:
                    * bpm
                    * ms
                    * hz

                Defaults to hz.
            bpm (float): set BPM (from 30 to 300)

                Defaults to 120.
            ms (int): set ms (from 10 to 2000)

                Defaults to 500.
            hz (float): set frequency (from 0.01 to 100)

                Defaults to 2.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="apulsator",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "mode": mode,
                "amount": amount,
                "offset_l": offset_l,
                "offset_r": offset_r,
                "width": width,
                "timing": timing,
                "bpm": bpm,
                "ms": ms,
                "hz": hz,
            },
        )[0]

    def arealtime(
        self, limit: str | None = None, speed: float | None = None
    ) -> "Stream":
        """Slow down filtering to match realtime.

        Args:
            limit (str): sleep time limit

                Defaults to 2.
            speed (float): speed factor (from DBL_MIN to DBL_MAX)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="arealtime",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "speed": speed,
            },
        )[0]

    def aresample(self, sample_rate: int | None = None) -> "Stream":
        """Resample audio data.

        Args:
            sample_rate (int): (from 0 to INT_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aresample",
            inputs=[self],
            named_arguments={
                "sample_rate": sample_rate,
            },
        )[0]

    def areverse(
        self,
    ) -> "Stream":
        """Reverse an audio clip.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="areverse", inputs=[self], named_arguments={}
        )[0]

    def arls(
        self,
        desired_stream: "Stream",
        order: int | None = None,
        lambda_: float | None = None,
        delta: float | None = None,
        out_mode: Literal["i", "d", "o", "n", "e"] | int | None = None,
        precision: Literal["auto", "float", "double"] | int | None = None,
    ) -> "Stream":
        """Apply Recursive Least Squares algorithm to first audio stream.

        Args:
            desired_stream (Stream): Input audio stream.
            order (int): set the filter order (from 1 to 32767)

                Defaults to 16.
            lambda_ (float): set the filter lambda (from 0 to 1)

                Defaults to 1.
            delta (float): set the filter delta (from 0 to 32767)

                Defaults to 2.
            out_mode (int | str): set output mode (from 0 to 4)

                Allowed values:
                    * i: input
                    * d: desired
                    * o: output
                    * n: noise
                    * e: error

                Defaults to o.
            precision (int | str): set processing precision (from 0 to 2)

                Allowed values:
                    * auto: set auto processing precision
                    * float: set single-floating point processing precision
                    * double: set double-floating point processing precision

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="arls",
            inputs=[self, desired_stream],
            named_arguments={
                "order": order,
                "lambda": lambda_,
                "delta": delta,
                "out_mode": out_mode,
                "precision": precision,
            },
        )[0]

    def arnndn(
        self, model: str | None = None, m: str | None = None, mix: float | None = None
    ) -> "Stream":
        """Reduce noise from speech using Recurrent Neural Networks.

        Args:
            model (str): set model name

            m (str): set model name

            mix (float): set output vs input mix (from -1 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="arnndn",
            inputs=[self],
            named_arguments={
                "model": model,
                "m": m,
                "mix": mix,
            },
        )[0]

    def asdr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Signal-to-Distortion Ratio.

        Args:
            input1_stream (Stream): Input audio stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asdr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def asegment(
        self, timestamps: str | None = None, samples: str | None = None
    ) -> "FilterMultiOutput":
        """Segment audio stream.

        Args:
            timestamps (str): timestamps of input at which to split input

            samples (str): samples at which to split input


        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="asegment",
            inputs=[self],
            named_arguments={
                "timestamps": timestamps,
                "samples": samples,
            },
        )

    def aselect(
        self,
        expr: str | None = None,
        e: str | None = None,
        outputs: int | None = None,
        n: int | None = None,
    ) -> "FilterMultiOutput":
        """Select audio frames to pass in output.

        Args:
            expr (str): set an expression to use for selecting frames

                Defaults to 1.
            e (str): set an expression to use for selecting frames

                Defaults to 1.
            outputs (int): set the number of outputs (from 1 to INT_MAX)

                Defaults to 1.
            n (int): set the number of outputs (from 1 to INT_MAX)

                Defaults to 1.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="aselect",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "e": e,
                "outputs": outputs,
                "n": n,
            },
        )

    def asendcmd(
        self,
        commands: str | None = None,
        c: str | None = None,
        filename: str | None = None,
        f: str | None = None,
    ) -> "Stream":
        """Send commands to filters.

        Args:
            commands (str): set commands

            c (str): set commands

            filename (str): set commands file

            f (str): set commands file


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asendcmd",
            inputs=[self],
            named_arguments={
                "commands": commands,
                "c": c,
                "filename": filename,
                "f": f,
            },
        )[0]

    def asetnsamples(
        self,
        nb_out_samples: int | None = None,
        n: int | None = None,
        pad: bool | None = None,
        p: bool | None = None,
    ) -> "Stream":
        """Set the number of samples for each output audio frames.

        Args:
            nb_out_samples (int): set the number of per-frame output samples (from 1 to INT_MAX)

                Defaults to 1024.
            n (int): set the number of per-frame output samples (from 1 to INT_MAX)

                Defaults to 1024.
            pad (bool): pad last frame with zeros

                Defaults to true.
            p (bool): pad last frame with zeros

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asetnsamples",
            inputs=[self],
            named_arguments={
                "nb_out_samples": nb_out_samples,
                "n": n,
                "pad": pad,
                "p": p,
            },
        )[0]

    def asetpts(self, expr: str | None = None) -> "Stream":
        """Set PTS for the output audio frame.

        Args:
            expr (str): Expression determining the frame timestamp

                Defaults to PTS.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asetpts",
            inputs=[self],
            named_arguments={
                "expr": expr,
            },
        )[0]

    def asetrate(
        self, sample_rate: int | None = None, r: int | None = None
    ) -> "Stream":
        """Change the sample rate without altering the data.

        Args:
            sample_rate (int): set the sample rate (from 1 to INT_MAX)

                Defaults to 44100.
            r (int): set the sample rate (from 1 to INT_MAX)

                Defaults to 44100.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asetrate",
            inputs=[self],
            named_arguments={
                "sample_rate": sample_rate,
                "r": r,
            },
        )[0]

    def asettb(self, expr: str | None = None, tb: str | None = None) -> "Stream":
        """Set timebase for the audio output link.

        Args:
            expr (str): set expression determining the output timebase

                Defaults to intb.
            tb (str): set expression determining the output timebase

                Defaults to intb.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asettb",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "tb": tb,
            },
        )[0]

    def ashowinfo(
        self,
    ) -> "Stream":
        """Show textual information for each audio frame.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ashowinfo", inputs=[self], named_arguments={}
        )[0]

    def asidedata(
        self,
        mode: Literal["select", "delete"] | int | None = None,
        type: Literal[
            "PANSCAN",
            "A53_CC",
            "STEREO3D",
            "MATRIXENCODING",
            "DOWNMIX_INFO",
            "REPLAYGAIN",
            "DISPLAYMATRIX",
            "AFD",
            "MOTION_VECTORS",
            "SKIP_SAMPLES",
            "AUDIO_SERVICE_TYPE",
            "MASTERING_DISPLAY_METADATA",
            "GOP_TIMECODE",
            "SPHERICAL",
            "CONTENT_LIGHT_LEVEL",
            "ICC_PROFILE",
            "S12M_TIMECOD",
            "DYNAMIC_HDR_PLUS",
            "REGIONS_OF_INTEREST",
            "VIDEO_ENC_PARAMS",
            "SEI_UNREGISTERED",
            "FILM_GRAIN_PARAMS",
            "DETECTION_BOUNDING_BOXES",
            "DETECTION_BBOXES",
            "DOVI_RPU_BUFFER",
            "DOVI_METADATA",
            "DYNAMIC_HDR_VIVID",
            "AMBIENT_VIEWING_ENVIRONMENT",
            "VIDEO_HINT",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Manipulate audio frame side data.

        Args:
            mode (int | str): set a mode of operation (from 0 to 1)

                Allowed values:
                    * select: select frame
                    * delete: delete side data

                Defaults to select.
            type (int | str): set side data type (from -1 to INT_MAX)

                Allowed values:
                    * PANSCAN
                    * A53_CC
                    * STEREO3D
                    * MATRIXENCODING
                    * DOWNMIX_INFO
                    * REPLAYGAIN
                    * DISPLAYMATRIX
                    * AFD
                    * MOTION_VECTORS
                    * SKIP_SAMPLES
                    * AUDIO_SERVICE_TYPE
                    * MASTERING_DISPLAY_METADATA
                    * GOP_TIMECODE
                    * SPHERICAL
                    * CONTENT_LIGHT_LEVEL
                    * ICC_PROFILE
                    * S12M_TIMECOD
                    * DYNAMIC_HDR_PLUS
                    * REGIONS_OF_INTEREST
                    * VIDEO_ENC_PARAMS
                    * SEI_UNREGISTERED
                    * FILM_GRAIN_PARAMS
                    * DETECTION_BOUNDING_BOXES
                    * DETECTION_BBOXES
                    * DOVI_RPU_BUFFER
                    * DOVI_METADATA
                    * DYNAMIC_HDR_VIVID
                    * AMBIENT_VIEWING_ENVIRONMENT
                    * VIDEO_HINT

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asidedata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "type": type,
            },
        )[0]

    def asisdr(self, input1_stream: "Stream") -> "Stream":
        """Measure Audio Scale-Invariant Signal-to-Distortion Ratio.

        Args:
            input1_stream (Stream): Input audio stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asisdr", inputs=[self, input1_stream], named_arguments={}
        )[0]

    def asoftclip(
        self,
        type: Literal[
            "hard", "tanh", "atan", "cubic", "exp", "alg", "quintic", "sin", "erf"
        ]
        | int
        | None = None,
        threshold: float | None = None,
        output: float | None = None,
        param: float | None = None,
        oversample: int | None = None,
    ) -> "Stream":
        """Audio Soft Clipper.

        Args:
            type (int | str): set softclip type (from -1 to 7)

                Allowed values:
                    * hard
                    * tanh
                    * atan
                    * cubic
                    * exp
                    * alg
                    * quintic
                    * sin
                    * erf

                Defaults to tanh.
            threshold (float): set softclip threshold (from 1e-06 to 1)

                Defaults to 1.
            output (float): set softclip output gain (from 1e-06 to 16)

                Defaults to 1.
            param (float): set softclip parameter (from 0.01 to 3)

                Defaults to 1.
            oversample (int): set oversample factor (from 1 to 64)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asoftclip",
            inputs=[self],
            named_arguments={
                "type": type,
                "threshold": threshold,
                "output": output,
                "param": param,
                "oversample": oversample,
            },
        )[0]

    def aspectralstats(
        self,
        win_size: int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        overlap: float | None = None,
        measure: Literal[
            "none",
            "all",
            "mean",
            "variance",
            "centroid",
            "spread",
            "skewness",
            "kurtosis",
            "entropy",
            "flatness",
            "crest",
            "flux",
            "slope",
            "decrease",
            "rolloff",
        ]
        | None = None,
    ) -> "Stream":
        """Show frequency domain statistics about audio frames.

        Args:
            win_size (int): set the window size (from 32 to 65536)

                Defaults to 2048.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 0.5.
            measure (str): select the parameters which are measured

                Allowed values:
                    * none
                    * all
                    * mean
                    * variance
                    * centroid
                    * spread
                    * skewness
                    * kurtosis
                    * entropy
                    * flatness
                    * crest
                    * flux
                    * slope
                    * decrease
                    * rolloff

                Defaults to all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="aspectralstats",
            inputs=[self],
            named_arguments={
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "measure": measure,
            },
        )[0]

    def asplit(self, outputs: int | None = None) -> "FilterMultiOutput":
        """Pass on the audio input to N audio outputs.

        Args:
            outputs (int): set number of outputs (from 1 to INT_MAX)

                Defaults to 2.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="asplit",
            inputs=[self],
            named_arguments={
                "outputs": outputs,
            },
        )

    def ass(
        self,
        filename: str | None = None,
        f: str | None = None,
        original_size: str | None = None,
        fontsdir: str | None = None,
        alpha: bool | None = None,
        shaping: Literal["auto", "simple", "complex"] | int | None = None,
    ) -> "Stream":
        """Render ASS subtitles onto input video using the libass library.

        Args:
            filename (str): set the filename of file to read

            f (str): set the filename of file to read

            original_size (str): set the size of the original video (used to scale fonts)

            fontsdir (str): set the directory containing the fonts to read

            alpha (bool): enable processing of alpha channel

                Defaults to false.
            shaping (int | str): set shaping engine (from -1 to 1)

                Allowed values:
                    * auto
                    * simple: simple shaping
                    * complex: complex shaping

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ass",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
                "original_size": original_size,
                "fontsdir": fontsdir,
                "alpha": alpha,
                "shaping": shaping,
            },
        )[0]

    def astats(
        self,
        length: float | None = None,
        metadata: bool | None = None,
        reset: int | None = None,
        measure_perchannel: Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ]
        | None = None,
        measure_overall: Literal[
            "none",
            "all",
            "Bit_depth",
            "Crest_factor",
            "DC_offset",
            "Dynamic_range",
            "Entropy",
            "Flat_factor",
            "Max_difference",
            "Max_level",
            "Mean_difference",
            "Min_difference",
            "Min_level",
            "Noise_floor",
            "Noise_floor_count",
            "Number_of_Infs",
            "Number_of_NaNs",
            "Number_of_denormals",
            "Number_of_samples",
            "Peak_count",
            "Peak_level",
            "RMS_difference",
            "RMS_level",
            "RMS_peak",
            "RMS_trough",
            "Zero_crossings",
            "Zero_crossings_rate",
            "Abs_Peak_count",
        ]
        | None = None,
    ) -> "Stream":
        """Show time domain statistics about audio frames.

        Args:
            length (float): set the window length (from 0 to 10)

                Defaults to 0.05.
            metadata (bool): inject metadata in the filtergraph

                Defaults to false.
            reset (int): Set the number of frames over which cumulative stats are calculated before being reset (from 0 to INT_MAX)

                Defaults to 0.
            measure_perchannel (str): Select the parameters which are measured per channel

                Allowed values:
                    * none
                    * all
                    * Bit_depth
                    * Crest_factor
                    * DC_offset
                    * Dynamic_range
                    * Entropy
                    * Flat_factor
                    * Max_difference
                    * Max_level
                    * Mean_difference
                    * Min_difference
                    * Min_level
                    * Noise_floor
                    * Noise_floor_count
                    * Number_of_Infs
                    * Number_of_NaNs
                    * Number_of_denormals
                    * Number_of_samples
                    * Peak_count
                    * Peak_level
                    * RMS_difference
                    * RMS_level
                    * RMS_peak
                    * RMS_trough
                    * Zero_crossings
                    * Zero_crossings_rate
                    * Abs_Peak_count

                Defaults to all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count.
            measure_overall (str): Select the parameters which are measured overall

                Allowed values:
                    * none
                    * all
                    * Bit_depth
                    * Crest_factor
                    * DC_offset
                    * Dynamic_range
                    * Entropy
                    * Flat_factor
                    * Max_difference
                    * Max_level
                    * Mean_difference
                    * Min_difference
                    * Min_level
                    * Noise_floor
                    * Noise_floor_count
                    * Number_of_Infs
                    * Number_of_NaNs
                    * Number_of_denormals
                    * Number_of_samples
                    * Peak_count
                    * Peak_level
                    * RMS_difference
                    * RMS_level
                    * RMS_peak
                    * RMS_trough
                    * Zero_crossings
                    * Zero_crossings_rate
                    * Abs_Peak_count

                Defaults to all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="astats",
            inputs=[self],
            named_arguments={
                "length": length,
                "metadata": metadata,
                "reset": reset,
                "measure_perchannel": measure_perchannel,
                "measure_overall": measure_overall,
            },
        )[0]

    def astreamselect(
        self, *streams: "Stream", inputs: int | None = None, map: str | None = None
    ) -> "FilterMultiOutput":
        """Select audio streams

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): number of input streams (from 2 to INT_MAX)

                Defaults to 2.
            map (str): input indexes to remap to outputs


        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="astreamselect",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "map": map,
            },
        )

    def asubboost(
        self,
        dry: float | None = None,
        wet: float | None = None,
        boost: float | None = None,
        decay: float | None = None,
        feedback: float | None = None,
        cutoff: float | None = None,
        slope: float | None = None,
        delay: float | None = None,
        channels: str | None = None,
    ) -> "Stream":
        """Boost subwoofer frequencies.

        Args:
            dry (float): set dry gain (from 0 to 1)

                Defaults to 1.
            wet (float): set wet gain (from 0 to 1)

                Defaults to 1.
            boost (float): set max boost (from 1 to 12)

                Defaults to 2.
            decay (float): set decay (from 0 to 1)

                Defaults to 0.
            feedback (float): set feedback (from 0 to 1)

                Defaults to 0.9.
            cutoff (float): set cutoff (from 50 to 900)

                Defaults to 100.
            slope (float): set slope (from 0.0001 to 1)

                Defaults to 0.5.
            delay (float): set delay (from 1 to 100)

                Defaults to 20.
            channels (str): set channels to filter

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asubboost",
            inputs=[self],
            named_arguments={
                "dry": dry,
                "wet": wet,
                "boost": boost,
                "decay": decay,
                "feedback": feedback,
                "cutoff": cutoff,
                "slope": slope,
                "delay": delay,
                "channels": channels,
            },
        )[0]

    def asubcut(
        self,
        cutoff: float | None = None,
        order: int | None = None,
        level: float | None = None,
    ) -> "Stream":
        """Cut subwoofer frequencies.

        Args:
            cutoff (float): set cutoff frequency (from 2 to 200)

                Defaults to 20.
            order (int): set filter order (from 3 to 20)

                Defaults to 10.
            level (float): set input level (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asubcut",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            },
        )[0]

    def asupercut(
        self,
        cutoff: float | None = None,
        order: int | None = None,
        level: float | None = None,
    ) -> "Stream":
        """Cut super frequencies.

        Args:
            cutoff (float): set cutoff frequency (from 20000 to 192000)

                Defaults to 20000.
            order (int): set filter order (from 3 to 20)

                Defaults to 10.
            level (float): set input level (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asupercut",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "order": order,
                "level": level,
            },
        )[0]

    def asuperpass(
        self,
        centerf: float | None = None,
        order: int | None = None,
        qfactor: float | None = None,
        level: float | None = None,
    ) -> "Stream":
        """Apply high order Butterworth band-pass filter.

        Args:
            centerf (float): set center frequency (from 2 to 999999)

                Defaults to 1000.
            order (int): set filter order (from 4 to 20)

                Defaults to 4.
            qfactor (float): set Q-factor (from 0.01 to 100)

                Defaults to 1.
            level (float): set input level (from 0 to 2)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asuperpass",
            inputs=[self],
            named_arguments={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            },
        )[0]

    def asuperstop(
        self,
        centerf: float | None = None,
        order: int | None = None,
        qfactor: float | None = None,
        level: float | None = None,
    ) -> "Stream":
        """Apply high order Butterworth band-stop filter.

        Args:
            centerf (float): set center frequency (from 2 to 999999)

                Defaults to 1000.
            order (int): set filter order (from 4 to 20)

                Defaults to 4.
            qfactor (float): set Q-factor (from 0.01 to 100)

                Defaults to 1.
            level (float): set input level (from 0 to 2)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="asuperstop",
            inputs=[self],
            named_arguments={
                "centerf": centerf,
                "order": order,
                "qfactor": qfactor,
                "level": level,
            },
        )[0]

    def atadenoise(
        self,
        _0a: float | None = None,
        _0b: float | None = None,
        _1a: float | None = None,
        _1b: float | None = None,
        _2a: float | None = None,
        _2b: float | None = None,
        s: int | None = None,
        p: str | None = None,
        a: Literal["p", "s"] | int | None = None,
        _0s: float | None = None,
        _1s: float | None = None,
        _2s: float | None = None,
    ) -> "Stream":
        """Apply an Adaptive Temporal Averaging Denoiser.

        Args:
            _0a (float): set threshold A for 1st plane (from 0 to 0.3)

                Defaults to 0.02.
            _0b (float): set threshold B for 1st plane (from 0 to 5)

                Defaults to 0.04.
            _1a (float): set threshold A for 2nd plane (from 0 to 0.3)

                Defaults to 0.02.
            _1b (float): set threshold B for 2nd plane (from 0 to 5)

                Defaults to 0.04.
            _2a (float): set threshold A for 3rd plane (from 0 to 0.3)

                Defaults to 0.02.
            _2b (float): set threshold B for 3rd plane (from 0 to 5)

                Defaults to 0.04.
            s (int): set how many frames to use (from 5 to 129)

                Defaults to 9.
            p (str): set what planes to filter

                Defaults to 7.
            a (int | str): set variant of algorithm (from 0 to 1)

                Allowed values:
                    * p: parallel
                    * s: serial

                Defaults to p.
            _0s (float): set sigma for 1st plane (from 0 to 32767)

                Defaults to 32767.
            _1s (float): set sigma for 2nd plane (from 0 to 32767)

                Defaults to 32767.
            _2s (float): set sigma for 3rd plane (from 0 to 32767)

                Defaults to 32767.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="atadenoise",
            inputs=[self],
            named_arguments={
                "0a": _0a,
                "0b": _0b,
                "1a": _1a,
                "1b": _1b,
                "2a": _2a,
                "2b": _2b,
                "s": s,
                "p": p,
                "a": a,
                "0s": _0s,
                "1s": _1s,
                "2s": _2s,
            },
        )[0]

    def atempo(self, tempo: float | None = None) -> "Stream":
        """Adjust audio tempo.

        Args:
            tempo (float): set tempo scale factor (from 0.5 to 100)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="atempo",
            inputs=[self],
            named_arguments={
                "tempo": tempo,
            },
        )[0]

    def atilt(
        self,
        freq: float | None = None,
        slope: float | None = None,
        width: float | None = None,
        order: int | None = None,
        level: float | None = None,
    ) -> "Stream":
        """Apply spectral tilt to audio.

        Args:
            freq (float): set central frequency (from 20 to 192000)

                Defaults to 10000.
            slope (float): set filter slope (from -1 to 1)

                Defaults to 0.
            width (float): set filter width (from 100 to 10000)

                Defaults to 1000.
            order (int): set filter order (from 2 to 30)

                Defaults to 5.
            level (float): set input level (from 0 to 4)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="atilt",
            inputs=[self],
            named_arguments={
                "freq": freq,
                "slope": slope,
                "width": width,
                "order": order,
                "level": level,
            },
        )[0]

    def atrim(
        self,
        start: str | None = None,
        starti: str | None = None,
        end: str | None = None,
        endi: str | None = None,
        start_pts: str | None = None,
        end_pts: str | None = None,
        duration: str | None = None,
        durationi: str | None = None,
        start_sample: str | None = None,
        end_sample: str | None = None,
    ) -> "Stream":
        """Pick one continuous section from the input, drop the rest.

        Args:
            start (str): Timestamp of the first frame that should be passed

                Defaults to INT64_MAX.
            starti (str): Timestamp of the first frame that should be passed

                Defaults to INT64_MAX.
            end (str): Timestamp of the first frame that should be dropped again

                Defaults to INT64_MAX.
            endi (str): Timestamp of the first frame that should be dropped again

                Defaults to INT64_MAX.
            start_pts (str): Timestamp of the first frame that should be  passed (from I64_MIN to I64_MAX)

                Defaults to I64_MIN.
            end_pts (str): Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX)

                Defaults to I64_MIN.
            duration (str): Maximum duration of the output

                Defaults to 0.
            durationi (str): Maximum duration of the output

                Defaults to 0.
            start_sample (str): Number of the first audio sample that should be passed to the output (from -1 to I64_MAX)

                Defaults to -1.
            end_sample (str): Number of the first audio sample that should be dropped again (from 0 to I64_MAX)

                Defaults to I64_MAX.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="atrim",
            inputs=[self],
            named_arguments={
                "start": start,
                "starti": starti,
                "end": end,
                "endi": endi,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "durationi": durationi,
                "start_sample": start_sample,
                "end_sample": end_sample,
            },
        )[0]

    def avectorscope(
        self,
        mode: Literal["lissajous", "lissajous_xy", "polar"] | int | None = None,
        m: Literal["lissajous", "lissajous_xy", "polar"] | int | None = None,
        rate: str | None = None,
        r: str | None = None,
        size: str | None = None,
        s: str | None = None,
        rc: int | None = None,
        gc: int | None = None,
        bc: int | None = None,
        ac: int | None = None,
        rf: int | None = None,
        gf: int | None = None,
        bf: int | None = None,
        af: int | None = None,
        zoom: float | None = None,
        draw: Literal["dot", "line", "aaline"] | int | None = None,
        scale: Literal["lin", "sqrt", "cbrt", "log"] | int | None = None,
        swap: bool | None = None,
        mirror: Literal["none", "x", "y", "xy"] | int | None = None,
    ) -> "Stream":
        """Convert input audio to vectorscope video output.

        Args:
            mode (int | str): set mode (from 0 to 2)

                Allowed values:
                    * lissajous
                    * lissajous_xy
                    * polar

                Defaults to lissajous.
            m (int | str): set mode (from 0 to 2)

                Allowed values:
                    * lissajous
                    * lissajous_xy
                    * polar

                Defaults to lissajous.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            size (str): set video size

                Defaults to 400x400.
            s (str): set video size

                Defaults to 400x400.
            rc (int): set red contrast (from 0 to 255)

                Defaults to 40.
            gc (int): set green contrast (from 0 to 255)

                Defaults to 160.
            bc (int): set blue contrast (from 0 to 255)

                Defaults to 80.
            ac (int): set alpha contrast (from 0 to 255)

                Defaults to 255.
            rf (int): set red fade (from 0 to 255)

                Defaults to 15.
            gf (int): set green fade (from 0 to 255)

                Defaults to 10.
            bf (int): set blue fade (from 0 to 255)

                Defaults to 5.
            af (int): set alpha fade (from 0 to 255)

                Defaults to 5.
            zoom (float): set zoom factor (from 0 to 10)

                Defaults to 1.
            draw (int | str): set draw mode (from 0 to 2)

                Allowed values:
                    * dot: draw dots
                    * line: draw lines
                    * aaline: draw anti-aliased lines

                Defaults to dot.
            scale (int | str): set amplitude scale mode (from 0 to 3)

                Allowed values:
                    * lin: linear
                    * sqrt: square root
                    * cbrt: cube root
                    * log: logarithmic

                Defaults to lin.
            swap (bool): swap x axis with y axis

                Defaults to true.
            mirror (int | str): mirror axis (from 0 to 3)

                Allowed values:
                    * none: no mirror
                    * x: mirror x
                    * y: mirror y
                    * xy: mirror both

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="avectorscope",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "rate": rate,
                "r": r,
                "size": size,
                "s": s,
                "rc": rc,
                "gc": gc,
                "bc": bc,
                "ac": ac,
                "rf": rf,
                "gf": gf,
                "bf": bf,
                "af": af,
                "zoom": zoom,
                "draw": draw,
                "scale": scale,
                "swap": swap,
                "mirror": mirror,
            },
        )[0]

    def avgblur(
        self,
        sizeX: int | None = None,
        planes: int | None = None,
        sizeY: int | None = None,
    ) -> "Stream":
        """Apply Average Blur filter.

        Args:
            sizeX (int): set horizontal size (from 1 to 1024)

                Defaults to 1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            sizeY (int): set vertical size (from 0 to 1024)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="avgblur",
            inputs=[self],
            named_arguments={
                "sizeX": sizeX,
                "planes": planes,
                "sizeY": sizeY,
            },
        )[0]

    def axcorrelate(
        self,
        axcorrelate1_stream: "Stream",
        size: int | None = None,
        algo: Literal["slow", "fast", "best"] | int | None = None,
    ) -> "Stream":
        """Cross-correlate two audio streams.

        Args:
            axcorrelate1_stream (Stream): Input audio stream.
            size (int): set the segment size (from 2 to 131072)

                Defaults to 256.
            algo (int | str): set the algorithm (from 0 to 2)

                Allowed values:
                    * slow: slow algorithm
                    * fast: fast algorithm
                    * best: best algorithm

                Defaults to best.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="axcorrelate",
            inputs=[self, axcorrelate1_stream],
            named_arguments={
                "size": size,
                "algo": algo,
            },
        )[0]

    def azmq(self, bind_address: str | None = None, b: str | None = None) -> "Stream":
        """Receive commands through ZMQ and broker them to filters.

        Args:
            bind_address (str): set bind address

                Defaults to tcp://*:5555.
            b (str): set bind address

                Defaults to tcp://*:5555.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="azmq",
            inputs=[self],
            named_arguments={
                "bind_address": bind_address,
                "b": b,
            },
        )[0]

    def backgroundkey(
        self,
        threshold: float | None = None,
        similarity: float | None = None,
        blend: float | None = None,
    ) -> "Stream":
        """Turns a static background into transparency.

        Args:
            threshold (float): set the scene change threshold (from 0 to 1)

                Defaults to 0.08.
            similarity (float): set the similarity (from 0 to 1)

                Defaults to 0.1.
            blend (float): set the blend value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="backgroundkey",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def bandpass(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        csg: bool | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a two-pole Butterworth band-pass filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            csg (bool): use constant skirt gain

                Defaults to false.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bandpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "csg": csg,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bandreject(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a two-pole Butterworth band-reject filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bandreject",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bass(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Boost or cut lower frequencies.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 100.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 100.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bbox(self, min_val: int | None = None) -> "Stream":
        """Compute bounding box for each frame.

        Args:
            min_val (int): set minimum luminance value for bounding box (from 0 to 65535)

                Defaults to 16.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bbox",
            inputs=[self],
            named_arguments={
                "min_val": min_val,
            },
        )[0]

    def bench(self, action: Literal["start", "stop"] | int | None = None) -> "Stream":
        """Benchmark part of a filtergraph.

        Args:
            action (int | str): set action (from 0 to 1)

                Allowed values:
                    * start: start timer
                    * stop: stop timer

                Defaults to start.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bench",
            inputs=[self],
            named_arguments={
                "action": action,
            },
        )[0]

    def bilateral(
        self,
        sigmaS: float | None = None,
        sigmaR: float | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply Bilateral filter.

        Args:
            sigmaS (float): set spatial sigma (from 0 to 512)

                Defaults to 0.1.
            sigmaR (float): set range sigma (from 0 to 1)

                Defaults to 0.1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bilateral",
            inputs=[self],
            named_arguments={
                "sigmaS": sigmaS,
                "sigmaR": sigmaR,
                "planes": planes,
            },
        )[0]

    def biquad(
        self,
        a0: float | None = None,
        a1: float | None = None,
        a2: float | None = None,
        b0: float | None = None,
        b1: float | None = None,
        b2: float | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a biquad IIR filter with the given coefficients.

        Args:
            a0 (float): (from INT_MIN to INT_MAX)

                Defaults to 1.
            a1 (float): (from INT_MIN to INT_MAX)

                Defaults to 0.
            a2 (float): (from INT_MIN to INT_MAX)

                Defaults to 0.
            b0 (float): (from INT_MIN to INT_MAX)

                Defaults to 0.
            b1 (float): (from INT_MIN to INT_MAX)

                Defaults to 0.
            b2 (float): (from INT_MIN to INT_MAX)

                Defaults to 0.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="biquad",
            inputs=[self],
            named_arguments={
                "a0": a0,
                "a1": a1,
                "a2": a2,
                "b0": b0,
                "b1": b1,
                "b2": b2,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def bitplanenoise(
        self, bitplane: int | None = None, filter: bool | None = None
    ) -> "Stream":
        """Measure bit plane noise.

        Args:
            bitplane (int): set bit plane to use for measuring noise (from 1 to 16)

                Defaults to 1.
            filter (bool): show noisy pixels

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bitplanenoise",
            inputs=[self],
            named_arguments={
                "bitplane": bitplane,
                "filter": filter,
            },
        )[0]

    def blackdetect(
        self,
        d: float | None = None,
        black_min_duration: float | None = None,
        picture_black_ratio_th: float | None = None,
        pic_th: float | None = None,
        pixel_black_th: float | None = None,
        pix_th: float | None = None,
        alpha: bool | None = None,
    ) -> "Stream":
        """Detect video intervals that are (almost) black.

        Args:
            d (float): set minimum detected black duration in seconds (from 0 to DBL_MAX)

                Defaults to 2.
            black_min_duration (float): set minimum detected black duration in seconds (from 0 to DBL_MAX)

                Defaults to 2.
            picture_black_ratio_th (float): set the picture black ratio threshold (from 0 to 1)

                Defaults to 0.98.
            pic_th (float): set the picture black ratio threshold (from 0 to 1)

                Defaults to 0.98.
            pixel_black_th (float): set the pixel black threshold (from 0 to 1)

                Defaults to 0.1.
            pix_th (float): set the pixel black threshold (from 0 to 1)

                Defaults to 0.1.
            alpha (bool): check alpha instead of luma

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="blackdetect",
            inputs=[self],
            named_arguments={
                "d": d,
                "black_min_duration": black_min_duration,
                "picture_black_ratio_th": picture_black_ratio_th,
                "pic_th": pic_th,
                "pixel_black_th": pixel_black_th,
                "pix_th": pix_th,
                "alpha": alpha,
            },
        )[0]

    def blackframe(
        self,
        amount: int | None = None,
        threshold: int | None = None,
        thresh: int | None = None,
    ) -> "Stream":
        """Detect frames that are (almost) black.

        Args:
            amount (int): percentage of the pixels that have to be below the threshold for the frame to be considered black (from 0 to 100)

                Defaults to 98.
            threshold (int): threshold below which a pixel value is considered black (from 0 to 255)

                Defaults to 32.
            thresh (int): threshold below which a pixel value is considered black (from 0 to 255)

                Defaults to 32.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="blackframe",
            inputs=[self],
            named_arguments={
                "amount": amount,
                "threshold": threshold,
                "thresh": thresh,
            },
        )[0]

    def blend(
        self,
        bottom_stream: "Stream",
        c0_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c1_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c2_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c3_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        all_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c0_expr: str | None = None,
        c1_expr: str | None = None,
        c2_expr: str | None = None,
        c3_expr: str | None = None,
        all_expr: str | None = None,
        c0_opacity: float | None = None,
        c1_opacity: float | None = None,
        c2_opacity: float | None = None,
        c3_opacity: float | None = None,
        all_opacity: float | None = None,
    ) -> "Stream":
        """Blend two video frames into each other.

        Args:
            bottom_stream (Stream): Input video stream.
            c0_mode (int | str): set component #0 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c1_mode (int | str): set component #1 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c2_mode (int | str): set component #2 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c3_mode (int | str): set component #3 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            all_mode (int | str): set blend mode for all components (from -1 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to -1.
            c0_expr (str): set color component #0 expression

            c1_expr (str): set color component #1 expression

            c2_expr (str): set color component #2 expression

            c3_expr (str): set color component #3 expression

            all_expr (str): set expression for all color components

            c0_opacity (float): set color component #0 opacity (from 0 to 1)

                Defaults to 1.
            c1_opacity (float): set color component #1 opacity (from 0 to 1)

                Defaults to 1.
            c2_opacity (float): set color component #2 opacity (from 0 to 1)

                Defaults to 1.
            c3_opacity (float): set color component #3 opacity (from 0 to 1)

                Defaults to 1.
            all_opacity (float): set opacity for all color components (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="blend",
            inputs=[self, bottom_stream],
            named_arguments={
                "c0_mode": c0_mode,
                "c1_mode": c1_mode,
                "c2_mode": c2_mode,
                "c3_mode": c3_mode,
                "all_mode": all_mode,
                "c0_expr": c0_expr,
                "c1_expr": c1_expr,
                "c2_expr": c2_expr,
                "c3_expr": c3_expr,
                "all_expr": all_expr,
                "c0_opacity": c0_opacity,
                "c1_opacity": c1_opacity,
                "c2_opacity": c2_opacity,
                "c3_opacity": c3_opacity,
                "all_opacity": all_opacity,
            },
        )[0]

    def blockdetect(
        self,
        period_min: int | None = None,
        period_max: int | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Blockdetect filter.

        Args:
            period_min (int): Minimum period to search for (from 2 to 32)

                Defaults to 3.
            period_max (int): Maximum period to search for (from 2 to 64)

                Defaults to 24.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="blockdetect",
            inputs=[self],
            named_arguments={
                "period_min": period_min,
                "period_max": period_max,
                "planes": planes,
            },
        )[0]

    def blurdetect(
        self,
        high: float | None = None,
        low: float | None = None,
        radius: int | None = None,
        block_pct: int | None = None,
        block_width: int | None = None,
        block_height: int | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Blurdetect filter.

        Args:
            high (float): set high threshold (from 0 to 1)

                Defaults to 0.117647.
            low (float): set low threshold (from 0 to 1)

                Defaults to 0.0588235.
            radius (int): search radius for maxima detection (from 1 to 100)

                Defaults to 50.
            block_pct (int): block pooling threshold when calculating blurriness (from 1 to 100)

                Defaults to 80.
            block_width (int): block size for block-based abbreviation of blurriness (from -1 to INT_MAX)

                Defaults to -1.
            block_height (int): block size for block-based abbreviation of blurriness (from -1 to INT_MAX)

                Defaults to -1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="blurdetect",
            inputs=[self],
            named_arguments={
                "high": high,
                "low": low,
                "radius": radius,
                "block_pct": block_pct,
                "block_width": block_width,
                "block_height": block_height,
                "planes": planes,
            },
        )[0]

    def bm3d(
        self,
        *streams: "Stream",
        sigma: float | None = None,
        block: int | None = None,
        bstep: int | None = None,
        group: int | None = None,
        range: int | None = None,
        mstep: int | None = None,
        thmse: float | None = None,
        hdthr: float | None = None,
        estim: Literal["basic", "final"] | int | None = None,
        ref: bool | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Block-Matching 3D denoiser.

        Args:
            *streams (Stream): One or more input streams.
            sigma (float): set denoising strength (from 0 to 99999.9)

                Defaults to 1.
            block (int): set size of local patch (from 8 to 64)

                Defaults to 16.
            bstep (int): set sliding step for processing blocks (from 1 to 64)

                Defaults to 4.
            group (int): set maximal number of similar blocks (from 1 to 256)

                Defaults to 1.
            range (int): set block matching range (from 1 to INT_MAX)

                Defaults to 9.
            mstep (int): set step for block matching (from 1 to 64)

                Defaults to 1.
            thmse (float): set threshold of mean square error for block matching (from 0 to INT_MAX)

                Defaults to 0.
            hdthr (float): set hard threshold for 3D transfer domain (from 0 to INT_MAX)

                Defaults to 2.7.
            estim (int | str): set filtering estimation mode (from 0 to 1)

                Allowed values:
                    * basic: basic estimate
                    * final: final estimate

                Defaults to basic.
            ref (bool): have reference stream

                Defaults to false.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 7.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bm3d",
            inputs=[self, *streams],
            named_arguments={
                "sigma": sigma,
                "block": block,
                "bstep": bstep,
                "group": group,
                "range": range,
                "mstep": mstep,
                "thmse": thmse,
                "hdthr": hdthr,
                "estim": estim,
                "ref": ref,
                "planes": planes,
            },
        )[0]

    def boxblur(
        self,
        luma_radius: str | None = None,
        lr: str | None = None,
        luma_power: int | None = None,
        lp: int | None = None,
        chroma_radius: str | None = None,
        cr: str | None = None,
        chroma_power: int | None = None,
        cp: int | None = None,
        alpha_radius: str | None = None,
        ar: str | None = None,
        alpha_power: int | None = None,
        ap: int | None = None,
    ) -> "Stream":
        """Blur the input.

        Args:
            luma_radius (str): Radius of the luma blurring box

                Defaults to 2.
            lr (str): Radius of the luma blurring box

                Defaults to 2.
            luma_power (int): How many times should the boxblur be applied to luma (from 0 to INT_MAX)

                Defaults to 2.
            lp (int): How many times should the boxblur be applied to luma (from 0 to INT_MAX)

                Defaults to 2.
            chroma_radius (str): Radius of the chroma blurring box

            cr (str): Radius of the chroma blurring box

            chroma_power (int): How many times should the boxblur be applied to chroma (from -1 to INT_MAX)

                Defaults to -1.
            cp (int): How many times should the boxblur be applied to chroma (from -1 to INT_MAX)

                Defaults to -1.
            alpha_radius (str): Radius of the alpha blurring box

            ar (str): Radius of the alpha blurring box

            alpha_power (int): How many times should the boxblur be applied to alpha (from -1 to INT_MAX)

                Defaults to -1.
            ap (int): How many times should the boxblur be applied to alpha (from -1 to INT_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="boxblur",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_power": luma_power,
                "lp": lp,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_power": chroma_power,
                "cp": cp,
                "alpha_radius": alpha_radius,
                "ar": ar,
                "alpha_power": alpha_power,
                "ap": ap,
            },
        )[0]

    def buffersink(
        self,
        pix_fmts: str | None = None,
        color_spaces: str | None = None,
        color_ranges: Literal["pixel_formats", "colorspaces", "colorranges"]
        | None = None,
    ) -> "SinkNode":
        """Buffer video frames, and make them available to the end of the filter graph.

        Args:
            pix_fmts (str): set the supported pixel formats

            color_spaces (str): set the supported color spaces

            color_ranges (str): set the supported color ranges

                Allowed values:
                    * pixel_formats: array of supported pixel formats
                    * colorspaces: array of supported color spaces
                    * colorranges: array of supported color ranges


        Returns:
            "SinkNode": A SinkNode representing the sink (terminal node).
        """
        return self._apply_sink_filter(
            filter_name="buffersink",
            inputs=[self],
            named_arguments={
                "pix_fmts": pix_fmts,
                "color_spaces": color_spaces,
                "color_ranges": color_ranges,
            },
        )

    def bwdif(
        self,
        mode: Literal["send_frame", "send_field"] | int | None = None,
        parity: Literal["tff", "bff", "auto"] | int | None = None,
        deint: Literal["all", "interlaced"] | int | None = None,
    ) -> "Stream":
        """Deinterlace the input image.

        Args:
            mode (int | str): specify the interlacing mode (from 0 to 1)

                Allowed values:
                    * send_frame: send one frame for each frame
                    * send_field: send one frame for each field

                Defaults to send_field.
            parity (int | str): specify the assumed picture field parity (from -1 to 1)

                Allowed values:
                    * tff: assume top field first
                    * bff: assume bottom field first
                    * auto: auto detect parity

                Defaults to auto.
            deint (int | str): specify which frames to deinterlace (from 0 to 1)

                Allowed values:
                    * all: deinterlace all frames
                    * interlaced: only deinterlace frames marked as interlaced

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="bwdif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def cas(self, strength: float | None = None, planes: str | None = None) -> "Stream":
        """Contrast Adaptive Sharpen.

        Args:
            strength (float): set the sharpening strength (from 0 to 1)

                Defaults to 0.
            planes (str): set what planes to filter

                Defaults to 7.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="cas",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "planes": planes,
            },
        )[0]

    def ccrepack(
        self,
    ) -> "Stream":
        """Repack CEA-708 closed caption metadata

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ccrepack", inputs=[self], named_arguments={}
        )[0]

    def channelmap(
        self, map: str | None = None, channel_layout: str | None = None
    ) -> "Stream":
        """Remap audio channels.

        Args:
            map (str): A comma-separated list of input channel numbers in output order.

            channel_layout (str): Output channel layout.


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="channelmap",
            inputs=[self],
            named_arguments={
                "map": map,
                "channel_layout": channel_layout,
            },
        )[0]

    def channelsplit(
        self, channel_layout: str | None = None, channels: str | None = None
    ) -> "FilterMultiOutput":
        """Split audio into per-channel streams.

        Args:
            channel_layout (str): Input channel layout.

                Defaults to stereo.
            channels (str): Channels to extract.

                Defaults to all.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="channelsplit",
            inputs=[self],
            named_arguments={
                "channel_layout": channel_layout,
                "channels": channels,
            },
        )

    def chorus(
        self,
        in_gain: float | None = None,
        out_gain: float | None = None,
        delays: str | None = None,
        decays: str | None = None,
        speeds: str | None = None,
        depths: str | None = None,
    ) -> "Stream":
        """Add a chorus effect to the audio.

        Args:
            in_gain (float): set input gain (from 0 to 1)

                Defaults to 0.4.
            out_gain (float): set output gain (from 0 to 1)

                Defaults to 0.4.
            delays (str): set delays

            decays (str): set decays

            speeds (str): set speeds

            depths (str): set depths


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="chorus",
            inputs=[self],
            named_arguments={
                "in_gain": in_gain,
                "out_gain": out_gain,
                "delays": delays,
                "decays": decays,
                "speeds": speeds,
                "depths": depths,
            },
        )[0]

    def chromahold(
        self,
        color: str | None = None,
        similarity: float | None = None,
        blend: float | None = None,
        yuv: bool | None = None,
    ) -> "Stream":
        """Turns a certain color range into gray.

        Args:
            color (str): set the chromahold key color

                Defaults to black.
            similarity (float): set the chromahold similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the chromahold blend value (from 0 to 1)

                Defaults to 0.
            yuv (bool): color parameter is in yuv instead of rgb

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="chromahold",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            },
        )[0]

    def chromakey(
        self,
        color: str | None = None,
        similarity: float | None = None,
        blend: float | None = None,
        yuv: bool | None = None,
    ) -> "Stream":
        """Turns a certain color into transparency. Operates on YUV colors.

        Args:
            color (str): set the chromakey key color

                Defaults to black.
            similarity (float): set the chromakey similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the chromakey key blend value (from 0 to 1)

                Defaults to 0.
            yuv (bool): color parameter is in yuv instead of rgb

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="chromakey",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
                "yuv": yuv,
            },
        )[0]

    def chromanr(
        self,
        thres: float | None = None,
        sizew: int | None = None,
        sizeh: int | None = None,
        stepw: int | None = None,
        steph: int | None = None,
        threy: float | None = None,
        threu: float | None = None,
        threv: float | None = None,
        distance: Literal["manhattan", "euclidean"] | int | None = None,
    ) -> "Stream":
        """Reduce chrominance noise.

        Args:
            thres (float): set y+u+v threshold (from 1 to 200)

                Defaults to 30.
            sizew (int): set horizontal patch size (from 1 to 100)

                Defaults to 5.
            sizeh (int): set vertical patch size (from 1 to 100)

                Defaults to 5.
            stepw (int): set horizontal step (from 1 to 50)

                Defaults to 1.
            steph (int): set vertical step (from 1 to 50)

                Defaults to 1.
            threy (float): set y threshold (from 1 to 200)

                Defaults to 200.
            threu (float): set u threshold (from 1 to 200)

                Defaults to 200.
            threv (float): set v threshold (from 1 to 200)

                Defaults to 200.
            distance (int | str): set distance type (from 0 to 1)

                Allowed values:
                    * manhattan
                    * euclidean

                Defaults to manhattan.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="chromanr",
            inputs=[self],
            named_arguments={
                "thres": thres,
                "sizew": sizew,
                "sizeh": sizeh,
                "stepw": stepw,
                "steph": steph,
                "threy": threy,
                "threu": threu,
                "threv": threv,
                "distance": distance,
            },
        )[0]

    def chromashift(
        self,
        cbh: int | None = None,
        cbv: int | None = None,
        crh: int | None = None,
        crv: int | None = None,
        edge: Literal["smear", "wrap"] | int | None = None,
    ) -> "Stream":
        """Shift chroma.

        Args:
            cbh (int): shift chroma-blue horizontally (from -255 to 255)

                Defaults to 0.
            cbv (int): shift chroma-blue vertically (from -255 to 255)

                Defaults to 0.
            crh (int): shift chroma-red horizontally (from -255 to 255)

                Defaults to 0.
            crv (int): shift chroma-red vertically (from -255 to 255)

                Defaults to 0.
            edge (int | str): set edge operation (from 0 to 1)

                Allowed values:
                    * smear
                    * wrap

                Defaults to smear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="chromashift",
            inputs=[self],
            named_arguments={
                "cbh": cbh,
                "cbv": cbv,
                "crh": crh,
                "crv": crv,
                "edge": edge,
            },
        )[0]

    def ciescope(
        self,
        system: Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ]
        | int
        | None = None,
        cie: Literal["xyy", "ucs", "luv"] | int | None = None,
        gamuts: Literal[
            "ntsc",
            "470m",
            "ebu",
            "470bg",
            "smpte",
            "240m",
            "apple",
            "widergb",
            "cie1931",
            "hdtv",
            "rec709",
            "uhdtv",
            "rec2020",
            "dcip3",
        ]
        | None = None,
        size: int | None = None,
        s: int | None = None,
        intensity: float | None = None,
        i: float | None = None,
        contrast: float | None = None,
        corrgamma: bool | None = None,
        showwhite: bool | None = None,
        gamma: float | None = None,
        fill: bool | None = None,
    ) -> "Stream":
        """Video CIE scope.

        Args:
            system (int | str): set color system (from 0 to 9)

                Allowed values:
                    * ntsc: NTSC 1953 Y'I'O' (ITU-R BT.470 System M)
                    * 470m: NTSC 1953 Y'I'O' (ITU-R BT.470 System M)
                    * ebu: EBU Y'U'V' (PAL/SECAM) (ITU-R BT.470 System B, G)
                    * 470bg: EBU Y'U'V' (PAL/SECAM) (ITU-R BT.470 System B, G)
                    * smpte: SMPTE-C RGB
                    * 240m: SMPTE-240M Y'PbPr
                    * apple: Apple RGB
                    * widergb: Adobe Wide Gamut RGB
                    * cie1931: CIE 1931 RGB
                    * hdtv: ITU.BT-709 Y'CbCr
                    * rec709: ITU.BT-709 Y'CbCr
                    * uhdtv: ITU-R.BT-2020
                    * rec2020: ITU-R.BT-2020
                    * dcip3: DCI-P3

                Defaults to hdtv.
            cie (int | str): set cie system (from 0 to 2)

                Allowed values:
                    * xyy: CIE 1931 xyY
                    * ucs: CIE 1960 UCS
                    * luv: CIE 1976 Luv

                Defaults to xyy.
            gamuts (str): set what gamuts to draw

                Allowed values:
                    * ntsc
                    * 470m
                    * ebu
                    * 470bg
                    * smpte
                    * 240m
                    * apple
                    * widergb
                    * cie1931
                    * hdtv
                    * rec709
                    * uhdtv
                    * rec2020
                    * dcip3

                Defaults to 0.
            size (int): set ciescope size (from 256 to 8192)

                Defaults to 512.
            s (int): set ciescope size (from 256 to 8192)

                Defaults to 512.
            intensity (float): set ciescope intensity (from 0 to 1)

                Defaults to 0.001.
            i (float): set ciescope intensity (from 0 to 1)

                Defaults to 0.001.
            contrast (float): (from 0 to 1)

                Defaults to 0.75.
            corrgamma (bool): No description available.

                Defaults to true.
            showwhite (bool): No description available.

                Defaults to false.
            gamma (float): (from 0.1 to 6)

                Defaults to 2.6.
            fill (bool): fill with CIE colors

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ciescope",
            inputs=[self],
            named_arguments={
                "system": system,
                "cie": cie,
                "gamuts": gamuts,
                "size": size,
                "s": s,
                "intensity": intensity,
                "i": i,
                "contrast": contrast,
                "corrgamma": corrgamma,
                "showwhite": showwhite,
                "gamma": gamma,
                "fill": fill,
            },
        )[0]

    def codecview(
        self,
        mv: Literal["pf", "bf", "bb"] | None = None,
        qp: bool | None = None,
        mv_type: Literal["fp", "bp"] | None = None,
        mvt: Literal["fp", "bp"] | None = None,
        frame_type: Literal["if", "pf", "bf"] | None = None,
        ft: Literal["if", "pf", "bf"] | None = None,
        block: bool | None = None,
    ) -> "Stream":
        """Visualize information about some codecs.

        Args:
            mv (str): set motion vectors to visualize

                Allowed values:
                    * pf: predicted MVs of P-frames
                    * bf: predicted MVs of B-frames
                    * bb: predicted MVs of B-frames

                Defaults to 0.
            qp (bool): No description available.

                Defaults to false.
            mv_type (str): set motion vectors type

                Allowed values:
                    * fp: predicted MVs
                    * bp: predicted MVs

                Defaults to 0.
            mvt (str): set motion vectors type

                Allowed values:
                    * fp: predicted MVs
                    * bp: predicted MVs

                Defaults to 0.
            frame_type (str): set frame types to visualize motion vectors of

                Allowed values:
                    * if
                    * pf
                    * bf

                Defaults to 0.
            ft (str): set frame types to visualize motion vectors of

                Allowed values:
                    * if
                    * pf
                    * bf

                Defaults to 0.
            block (bool): set block partitioning structure to visualize

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="codecview",
            inputs=[self],
            named_arguments={
                "mv": mv,
                "qp": qp,
                "mv_type": mv_type,
                "mvt": mvt,
                "frame_type": frame_type,
                "ft": ft,
                "block": block,
            },
        )[0]

    def colorbalance(
        self,
        rs: float | None = None,
        gs: float | None = None,
        bs: float | None = None,
        rm: float | None = None,
        gm: float | None = None,
        bm: float | None = None,
        rh: float | None = None,
        gh: float | None = None,
        bh: float | None = None,
        pl: bool | None = None,
    ) -> "Stream":
        """Adjust the color balance.

        Args:
            rs (float): set red shadows (from -1 to 1)

                Defaults to 0.
            gs (float): set green shadows (from -1 to 1)

                Defaults to 0.
            bs (float): set blue shadows (from -1 to 1)

                Defaults to 0.
            rm (float): set red midtones (from -1 to 1)

                Defaults to 0.
            gm (float): set green midtones (from -1 to 1)

                Defaults to 0.
            bm (float): set blue midtones (from -1 to 1)

                Defaults to 0.
            rh (float): set red highlights (from -1 to 1)

                Defaults to 0.
            gh (float): set green highlights (from -1 to 1)

                Defaults to 0.
            bh (float): set blue highlights (from -1 to 1)

                Defaults to 0.
            pl (bool): preserve lightness

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorbalance",
            inputs=[self],
            named_arguments={
                "rs": rs,
                "gs": gs,
                "bs": bs,
                "rm": rm,
                "gm": gm,
                "bm": bm,
                "rh": rh,
                "gh": gh,
                "bh": bh,
                "pl": pl,
            },
        )[0]

    def colorchannelmixer(
        self,
        rr: float | None = None,
        rg: float | None = None,
        rb: float | None = None,
        ra: float | None = None,
        gr: float | None = None,
        gg: float | None = None,
        gb: float | None = None,
        ga: float | None = None,
        br: float | None = None,
        bg: float | None = None,
        bb: float | None = None,
        ba: float | None = None,
        ar: float | None = None,
        ag: float | None = None,
        ab: float | None = None,
        aa: float | None = None,
        pc: Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"]
        | int
        | None = None,
        pa: float | None = None,
    ) -> "Stream":
        """Adjust colors by mixing color channels.

        Args:
            rr (float): set the red gain for the red channel (from -2 to 2)

                Defaults to 1.
            rg (float): set the green gain for the red channel (from -2 to 2)

                Defaults to 0.
            rb (float): set the blue gain for the red channel (from -2 to 2)

                Defaults to 0.
            ra (float): set the alpha gain for the red channel (from -2 to 2)

                Defaults to 0.
            gr (float): set the red gain for the green channel (from -2 to 2)

                Defaults to 0.
            gg (float): set the green gain for the green channel (from -2 to 2)

                Defaults to 1.
            gb (float): set the blue gain for the green channel (from -2 to 2)

                Defaults to 0.
            ga (float): set the alpha gain for the green channel (from -2 to 2)

                Defaults to 0.
            br (float): set the red gain for the blue channel (from -2 to 2)

                Defaults to 0.
            bg (float): set the green gain for the blue channel (from -2 to 2)

                Defaults to 0.
            bb (float): set the blue gain for the blue channel (from -2 to 2)

                Defaults to 1.
            ba (float): set the alpha gain for the blue channel (from -2 to 2)

                Defaults to 0.
            ar (float): set the red gain for the alpha channel (from -2 to 2)

                Defaults to 0.
            ag (float): set the green gain for the alpha channel (from -2 to 2)

                Defaults to 0.
            ab (float): set the blue gain for the alpha channel (from -2 to 2)

                Defaults to 0.
            aa (float): set the alpha gain for the alpha channel (from -2 to 2)

                Defaults to 1.
            pc (int | str): set the preserve color mode (from 0 to 6)

                Allowed values:
                    * none: disabled
                    * lum: luminance
                    * max: max
                    * avg: average
                    * sum: sum
                    * nrm: norm
                    * pwr: power

                Defaults to none.
            pa (float): set the preserve color amount (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorchannelmixer",
            inputs=[self],
            named_arguments={
                "rr": rr,
                "rg": rg,
                "rb": rb,
                "ra": ra,
                "gr": gr,
                "gg": gg,
                "gb": gb,
                "ga": ga,
                "br": br,
                "bg": bg,
                "bb": bb,
                "ba": ba,
                "ar": ar,
                "ag": ag,
                "ab": ab,
                "aa": aa,
                "pc": pc,
                "pa": pa,
            },
        )[0]

    def colorcontrast(
        self,
        rc: float | None = None,
        gm: float | None = None,
        by: float | None = None,
        rcw: float | None = None,
        gmw: float | None = None,
        byw: float | None = None,
        pl: float | None = None,
    ) -> "Stream":
        """Adjust color contrast between RGB components.

        Args:
            rc (float): set the red-cyan contrast (from -1 to 1)

                Defaults to 0.
            gm (float): set the green-magenta contrast (from -1 to 1)

                Defaults to 0.
            by (float): set the blue-yellow contrast (from -1 to 1)

                Defaults to 0.
            rcw (float): set the red-cyan weight (from 0 to 1)

                Defaults to 0.
            gmw (float): set the green-magenta weight (from 0 to 1)

                Defaults to 0.
            byw (float): set the blue-yellow weight (from 0 to 1)

                Defaults to 0.
            pl (float): set the amount of preserving lightness (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorcontrast",
            inputs=[self],
            named_arguments={
                "rc": rc,
                "gm": gm,
                "by": by,
                "rcw": rcw,
                "gmw": gmw,
                "byw": byw,
                "pl": pl,
            },
        )[0]

    def colorcorrect(
        self,
        rl: float | None = None,
        bl: float | None = None,
        rh: float | None = None,
        bh: float | None = None,
        saturation: float | None = None,
        analyze: Literal["manual", "average", "minmax", "median"] | int | None = None,
    ) -> "Stream":
        """Adjust color white balance selectively for blacks and whites.

        Args:
            rl (float): set the red shadow spot (from -1 to 1)

                Defaults to 0.
            bl (float): set the blue shadow spot (from -1 to 1)

                Defaults to 0.
            rh (float): set the red highlight spot (from -1 to 1)

                Defaults to 0.
            bh (float): set the blue highlight spot (from -1 to 1)

                Defaults to 0.
            saturation (float): set the amount of saturation (from -3 to 3)

                Defaults to 1.
            analyze (int | str): set the analyze mode (from 0 to 3)

                Allowed values:
                    * manual: manually set options
                    * average: use average pixels
                    * minmax: use minmax pixels
                    * median: use median pixels

                Defaults to manual.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorcorrect",
            inputs=[self],
            named_arguments={
                "rl": rl,
                "bl": bl,
                "rh": rh,
                "bh": bh,
                "saturation": saturation,
                "analyze": analyze,
            },
        )[0]

    def colordetect(
        self, mode: Literal["color_range", "alpha_mode", "all"] | None = None
    ) -> "Stream":
        """Detect video color properties.

        Args:
            mode (str): Image properties to detect

                Allowed values:
                    * color_range: (YUV) color range
                    * alpha_mode: alpha mode
                    * all: all supported properties

                Defaults to color_range+alpha_mode+all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colordetect",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def colorhold(
        self,
        color: str | None = None,
        similarity: float | None = None,
        blend: float | None = None,
    ) -> "Stream":
        """Turns a certain color range into gray. Operates on RGB colors.

        Args:
            color (str): set the colorhold key color

                Defaults to black.
            similarity (float): set the colorhold similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the colorhold blend value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorhold",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def colorize(
        self,
        hue: float | None = None,
        saturation: float | None = None,
        lightness: float | None = None,
        mix: float | None = None,
    ) -> "Stream":
        """Overlay a solid color on the video stream.

        Args:
            hue (float): set the hue (from 0 to 360)

                Defaults to 0.
            saturation (float): set the saturation (from 0 to 1)

                Defaults to 0.5.
            lightness (float): set the lightness (from 0 to 1)

                Defaults to 0.5.
            mix (float): set the mix of source lightness (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorize",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "saturation": saturation,
                "lightness": lightness,
                "mix": mix,
            },
        )[0]

    def colorkey(
        self,
        color: str | None = None,
        similarity: float | None = None,
        blend: float | None = None,
    ) -> "Stream":
        """Turns a certain color into transparency. Operates on RGB colors.

        Args:
            color (str): set the colorkey key color

                Defaults to black.
            similarity (float): set the colorkey similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the colorkey key blend value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorkey",
            inputs=[self],
            named_arguments={
                "color": color,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def colorlevels(
        self,
        rimin: float | None = None,
        gimin: float | None = None,
        bimin: float | None = None,
        aimin: float | None = None,
        rimax: float | None = None,
        gimax: float | None = None,
        bimax: float | None = None,
        aimax: float | None = None,
        romin: float | None = None,
        gomin: float | None = None,
        bomin: float | None = None,
        aomin: float | None = None,
        romax: float | None = None,
        gomax: float | None = None,
        bomax: float | None = None,
        aomax: float | None = None,
        preserve: Literal["none", "lum", "max", "avg", "sum", "nrm", "pwr"]
        | int
        | None = None,
    ) -> "Stream":
        """Adjust the color levels.

        Args:
            rimin (float): set input red black point (from -1 to 1)

                Defaults to 0.
            gimin (float): set input green black point (from -1 to 1)

                Defaults to 0.
            bimin (float): set input blue black point (from -1 to 1)

                Defaults to 0.
            aimin (float): set input alpha black point (from -1 to 1)

                Defaults to 0.
            rimax (float): set input red white point (from -1 to 1)

                Defaults to 1.
            gimax (float): set input green white point (from -1 to 1)

                Defaults to 1.
            bimax (float): set input blue white point (from -1 to 1)

                Defaults to 1.
            aimax (float): set input alpha white point (from -1 to 1)

                Defaults to 1.
            romin (float): set output red black point (from 0 to 1)

                Defaults to 0.
            gomin (float): set output green black point (from 0 to 1)

                Defaults to 0.
            bomin (float): set output blue black point (from 0 to 1)

                Defaults to 0.
            aomin (float): set output alpha black point (from 0 to 1)

                Defaults to 0.
            romax (float): set output red white point (from 0 to 1)

                Defaults to 1.
            gomax (float): set output green white point (from 0 to 1)

                Defaults to 1.
            bomax (float): set output blue white point (from 0 to 1)

                Defaults to 1.
            aomax (float): set output alpha white point (from 0 to 1)

                Defaults to 1.
            preserve (int | str): set preserve color mode (from 0 to 6)

                Allowed values:
                    * none: disabled
                    * lum: luminance
                    * max: max
                    * avg: average
                    * sum: sum
                    * nrm: norm
                    * pwr: power

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorlevels",
            inputs=[self],
            named_arguments={
                "rimin": rimin,
                "gimin": gimin,
                "bimin": bimin,
                "aimin": aimin,
                "rimax": rimax,
                "gimax": gimax,
                "bimax": bimax,
                "aimax": aimax,
                "romin": romin,
                "gomin": gomin,
                "bomin": bomin,
                "aomin": aomin,
                "romax": romax,
                "gomax": gomax,
                "bomax": bomax,
                "aomax": aomax,
                "preserve": preserve,
            },
        )[0]

    def colormap(
        self,
        source_stream: "Stream",
        target_stream: "Stream",
        patch_size: str | None = None,
        nb_patches: int | None = None,
        type: Literal["relative", "absolute"] | int | None = None,
        kernel: Literal["euclidean", "weuclidean"] | int | None = None,
    ) -> "Stream":
        """Apply custom Color Maps to video stream.

        Args:
            source_stream (Stream): Input video stream.
            target_stream (Stream): Input video stream.
            patch_size (str): set patch size

                Defaults to 64x64.
            nb_patches (int): set number of patches (from 0 to 64)

                Defaults to 0.
            type (int | str): set the target type used (from 0 to 1)

                Allowed values:
                    * relative: the target colors are relative
                    * absolute: the target colors are absolute

                Defaults to absolute.
            kernel (int | str): set the kernel used for measuring color difference (from 0 to 1)

                Allowed values:
                    * euclidean: square root of sum of squared differences
                    * weuclidean: weighted square root of sum of squared differences

                Defaults to euclidean.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colormap",
            inputs=[self, source_stream, target_stream],
            named_arguments={
                "patch_size": patch_size,
                "nb_patches": nb_patches,
                "type": type,
                "kernel": kernel,
            },
        )[0]

    def colormatrix(
        self,
        src: Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int
        | None = None,
        dst: Literal[
            "bt709",
            "fcc",
            "bt601",
            "bt470",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Convert color matrix.

        Args:
            src (int | str): set source color matrix (from -1 to 4)

                Allowed values:
                    * bt709: set BT.709 colorspace
                    * fcc: set FCC colorspace
                    * bt601: set BT.601 colorspace
                    * bt470: set BT.470 colorspace
                    * bt470bg: set BT.470 colorspace
                    * smpte170m: set SMTPE-170M colorspace
                    * smpte240m: set SMPTE-240M colorspace
                    * bt2020: set BT.2020 colorspace

                Defaults to -1.
            dst (int | str): set destination color matrix (from -1 to 4)

                Allowed values:
                    * bt709: set BT.709 colorspace
                    * fcc: set FCC colorspace
                    * bt601: set BT.601 colorspace
                    * bt470: set BT.470 colorspace
                    * bt470bg: set BT.470 colorspace
                    * smpte170m: set SMTPE-170M colorspace
                    * smpte240m: set SMPTE-240M colorspace
                    * bt2020: set BT.2020 colorspace

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colormatrix",
            inputs=[self],
            named_arguments={
                "src": src,
                "dst": dst,
            },
        )[0]

    def colorspace(
        self,
        all: Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int
        | None = None,
        space: Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | int
        | None = None,
        range: Literal["tv", "mpeg", "pc", "jpeg"] | int | None = None,
        primaries: Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        trc: Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | int
        | None = None,
        format: Literal[
            "yuv420p",
            "yuv420p10",
            "yuv420p12",
            "yuv422p",
            "yuv422p10",
            "yuv422p12",
            "yuv444p",
            "yuv444p10",
            "yuv444p12",
        ]
        | int
        | None = None,
        fast: bool | None = None,
        dither: Literal["none", "fsb"] | int | None = None,
        wpadapt: Literal["bradford", "vonkries", "identity"] | int | None = None,
        iall: Literal[
            "bt470m",
            "bt470bg",
            "bt601-6-525",
            "bt601-6-625",
            "bt709",
            "smpte170m",
            "smpte240m",
            "bt2020",
        ]
        | int
        | None = None,
        ispace: Literal[
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "gbr",
            "bt2020nc",
            "bt2020ncl",
        ]
        | int
        | None = None,
        irange: Literal["tv", "mpeg", "pc", "jpeg"] | int | None = None,
        iprimaries: Literal[
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "smpte428",
            "film",
            "smpte431",
            "smpte432",
            "bt2020",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        itrc: Literal[
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "srgb",
            "iec61966-2-1",
            "xvycc",
            "iec61966-2-4",
            "bt2020-10",
            "bt2020-12",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Convert between colorspaces.

        Args:
            all (int | str): Set all color properties together (from 0 to 8)

                Allowed values:
                    * bt470m
                    * bt470bg
                    * bt601-6-525
                    * bt601-6-625
                    * bt709
                    * smpte170m
                    * smpte240m
                    * bt2020

                Defaults to 0.
            space (int | str): Output colorspace (from 0 to 17)

                Allowed values:
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * gbr
                    * bt2020nc
                    * bt2020ncl

                Defaults to 2.
            range (int | str): Output color range (from 0 to 2)

                Allowed values:
                    * tv
                    * mpeg
                    * pc
                    * jpeg

                Defaults to 0.
            primaries (int | str): Output color primaries (from 0 to 22)

                Allowed values:
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * smpte428
                    * film
                    * smpte431
                    * smpte432
                    * bt2020
                    * jedec-p22
                    * ebu3213

                Defaults to 2.
            trc (int | str): Output transfer characteristics (from 0 to 18)

                Allowed values:
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * srgb
                    * iec61966-2-1
                    * xvycc
                    * iec61966-2-4
                    * bt2020-10
                    * bt2020-12

                Defaults to 2.
            format (int | str): Output pixel format (from -1 to 161)

                Allowed values:
                    * yuv420p
                    * yuv420p10
                    * yuv420p12
                    * yuv422p
                    * yuv422p10
                    * yuv422p12
                    * yuv444p
                    * yuv444p10
                    * yuv444p12

                Defaults to -1.
            fast (bool): Ignore primary chromaticity and gamma correction

                Defaults to false.
            dither (int | str): Dithering mode (from 0 to 1)

                Allowed values:
                    * none
                    * fsb

                Defaults to none.
            wpadapt (int | str): Whitepoint adaptation method (from 0 to 2)

                Allowed values:
                    * bradford
                    * vonkries
                    * identity

                Defaults to bradford.
            iall (int | str): Set all input color properties together (from 0 to 8)

                Allowed values:
                    * bt470m
                    * bt470bg
                    * bt601-6-525
                    * bt601-6-625
                    * bt709
                    * smpte170m
                    * smpte240m
                    * bt2020

                Defaults to 0.
            ispace (int | str): Input colorspace (from 0 to 22)

                Allowed values:
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * gbr
                    * bt2020nc
                    * bt2020ncl

                Defaults to 2.
            irange (int | str): Input color range (from 0 to 2)

                Allowed values:
                    * tv
                    * mpeg
                    * pc
                    * jpeg

                Defaults to 0.
            iprimaries (int | str): Input color primaries (from 0 to 22)

                Allowed values:
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * smpte428
                    * film
                    * smpte431
                    * smpte432
                    * bt2020
                    * jedec-p22
                    * ebu3213

                Defaults to 2.
            itrc (int | str): Input transfer characteristics (from 0 to 18)

                Allowed values:
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * srgb
                    * iec61966-2-1
                    * xvycc
                    * iec61966-2-4
                    * bt2020-10
                    * bt2020-12

                Defaults to 2.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colorspace",
            inputs=[self],
            named_arguments={
                "all": all,
                "space": space,
                "range": range,
                "primaries": primaries,
                "trc": trc,
                "format": format,
                "fast": fast,
                "dither": dither,
                "wpadapt": wpadapt,
                "iall": iall,
                "ispace": ispace,
                "irange": irange,
                "iprimaries": iprimaries,
                "itrc": itrc,
            },
        )[0]

    def colortemperature(
        self,
        temperature: float | None = None,
        mix: float | None = None,
        pl: float | None = None,
    ) -> "Stream":
        """Adjust color temperature of video.

        Args:
            temperature (float): set the temperature in Kelvin (from 1000 to 40000)

                Defaults to 6500.
            mix (float): set the mix with filtered output (from 0 to 1)

                Defaults to 1.
            pl (float): set the amount of preserving lightness (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="colortemperature",
            inputs=[self],
            named_arguments={
                "temperature": temperature,
                "mix": mix,
                "pl": pl,
            },
        )[0]

    def compand(
        self,
        attacks: str | None = None,
        decays: str | None = None,
        points: str | None = None,
        soft_knee: float | None = None,
        gain: float | None = None,
        volume: float | None = None,
        delay: float | None = None,
    ) -> "Stream":
        """Compress or expand audio dynamic range.

        Args:
            attacks (str): set time over which increase of volume is determined

                Defaults to 0.
            decays (str): set time over which decrease of volume is determined

                Defaults to 0.8.
            points (str): set points of transfer function

                Defaults to -70/-70|-60/-20|1/0.
            soft_knee (float): set soft-knee (from 0.01 to 900)

                Defaults to 0.01.
            gain (float): set output gain (from -900 to 900)

                Defaults to 0.
            volume (float): set initial volume (from -900 to 0)

                Defaults to 0.
            delay (float): set delay for samples before sending them to volume adjuster (from 0 to 20)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="compand",
            inputs=[self],
            named_arguments={
                "attacks": attacks,
                "decays": decays,
                "points": points,
                "soft-knee": soft_knee,
                "gain": gain,
                "volume": volume,
                "delay": delay,
            },
        )[0]

    def compensationdelay(
        self,
        mm: int | None = None,
        cm: int | None = None,
        m: int | None = None,
        dry: float | None = None,
        wet: float | None = None,
        temp: int | None = None,
    ) -> "Stream":
        """Audio Compensation Delay Line.

        Args:
            mm (int): set mm distance (from 0 to 10)

                Defaults to 0.
            cm (int): set cm distance (from 0 to 100)

                Defaults to 0.
            m (int): set meter distance (from 0 to 100)

                Defaults to 0.
            dry (float): set dry amount (from 0 to 1)

                Defaults to 0.
            wet (float): set wet amount (from 0 to 1)

                Defaults to 1.
            temp (int): set temperature °C (from -50 to 50)

                Defaults to 20.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="compensationdelay",
            inputs=[self],
            named_arguments={
                "mm": mm,
                "cm": cm,
                "m": m,
                "dry": dry,
                "wet": wet,
                "temp": temp,
            },
        )[0]

    def concat(
        self,
        *streams: "Stream",
        n: int | None = None,
        v: int | None = None,
        a: int | None = None,
        unsafe: bool | None = None,
    ) -> "FilterMultiOutput":
        """Concatenate audio and video streams.

        Args:
            *streams (Stream): One or more input streams.
            n (int): specify the number of segments (from 1 to INT_MAX)

                Defaults to 2.
            v (int): specify the number of video streams (from 0 to INT_MAX)

                Defaults to 1.
            a (int): specify the number of audio streams (from 0 to INT_MAX)

                Defaults to 0.
            unsafe (bool): enable unsafe mode

                Defaults to false.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="concat",
            inputs=[self, *streams],
            named_arguments={
                "n": n,
                "v": v,
                "a": a,
                "unsafe": unsafe,
            },
        )

    def convolution(
        self,
        _0m: str | None = None,
        _1m: str | None = None,
        _2m: str | None = None,
        _3m: str | None = None,
        _0rdiv: float | None = None,
        _1rdiv: float | None = None,
        _2rdiv: float | None = None,
        _3rdiv: float | None = None,
        _0bias: float | None = None,
        _1bias: float | None = None,
        _2bias: float | None = None,
        _3bias: float | None = None,
        _0mode: Literal["square", "row", "column"] | int | None = None,
        _1mode: Literal["square", "row", "column"] | int | None = None,
        _2mode: Literal["square", "row", "column"] | int | None = None,
        _3mode: Literal["square", "row", "column"] | int | None = None,
    ) -> "Stream":
        """Apply convolution filter.

        Args:
            _0m (str): set matrix for 1st plane

                Defaults to 0 0 0 0 1 0 0 0 0.
            _1m (str): set matrix for 2nd plane

                Defaults to 0 0 0 0 1 0 0 0 0.
            _2m (str): set matrix for 3rd plane

                Defaults to 0 0 0 0 1 0 0 0 0.
            _3m (str): set matrix for 4th plane

                Defaults to 0 0 0 0 1 0 0 0 0.
            _0rdiv (float): set rdiv for 1st plane (from 0 to INT_MAX)

                Defaults to 0.
            _1rdiv (float): set rdiv for 2nd plane (from 0 to INT_MAX)

                Defaults to 0.
            _2rdiv (float): set rdiv for 3rd plane (from 0 to INT_MAX)

                Defaults to 0.
            _3rdiv (float): set rdiv for 4th plane (from 0 to INT_MAX)

                Defaults to 0.
            _0bias (float): set bias for 1st plane (from 0 to INT_MAX)

                Defaults to 0.
            _1bias (float): set bias for 2nd plane (from 0 to INT_MAX)

                Defaults to 0.
            _2bias (float): set bias for 3rd plane (from 0 to INT_MAX)

                Defaults to 0.
            _3bias (float): set bias for 4th plane (from 0 to INT_MAX)

                Defaults to 0.
            _0mode (int | str): set matrix mode for 1st plane (from 0 to 2)

                Allowed values:
                    * square: square matrix
                    * row: single row matrix
                    * column: single column matrix

                Defaults to square.
            _1mode (int | str): set matrix mode for 2nd plane (from 0 to 2)

                Allowed values:
                    * square: square matrix
                    * row: single row matrix
                    * column: single column matrix

                Defaults to square.
            _2mode (int | str): set matrix mode for 3rd plane (from 0 to 2)

                Allowed values:
                    * square: square matrix
                    * row: single row matrix
                    * column: single column matrix

                Defaults to square.
            _3mode (int | str): set matrix mode for 4th plane (from 0 to 2)

                Allowed values:
                    * square: square matrix
                    * row: single row matrix
                    * column: single column matrix

                Defaults to square.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="convolution",
            inputs=[self],
            named_arguments={
                "0m": _0m,
                "1m": _1m,
                "2m": _2m,
                "3m": _3m,
                "0rdiv": _0rdiv,
                "1rdiv": _1rdiv,
                "2rdiv": _2rdiv,
                "3rdiv": _3rdiv,
                "0bias": _0bias,
                "1bias": _1bias,
                "2bias": _2bias,
                "3bias": _3bias,
                "0mode": _0mode,
                "1mode": _1mode,
                "2mode": _2mode,
                "3mode": _3mode,
            },
        )[0]

    def convolve(
        self,
        impulse_stream: "Stream",
        planes: int | None = None,
        impulse: Literal["first", "all"] | int | None = None,
        noise: float | None = None,
    ) -> "Stream":
        """Convolve first video stream with second video stream.

        Args:
            impulse_stream (Stream): Input video stream.
            planes (int): set planes to convolve (from 0 to 15)

                Defaults to 7.
            impulse (int | str): when to process impulses (from 0 to 1)

                Allowed values:
                    * first: process only first impulse, ignore rest
                    * all: process all impulses

                Defaults to all.
            noise (float): set noise (from 0 to 1)

                Defaults to 1e-07.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="convolve",
            inputs=[self, impulse_stream],
            named_arguments={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            },
        )[0]

    def copy(
        self,
    ) -> "Stream":
        """Copy the input video unchanged to the output.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="copy", inputs=[self], named_arguments={}
        )[0]

    def coreimage(
        self,
        list_filters: bool | None = None,
        list_generators: bool | None = None,
        filter: str | None = None,
        output_rect: str | None = None,
    ) -> "Stream":
        """Video filtering using CoreImage API.

        Args:
            list_filters (bool): list available filters

                Defaults to false.
            list_generators (bool): list available generators

                Defaults to false.
            filter (str): names and options of filters to apply

            output_rect (str): output rectangle within output image


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="coreimage",
            inputs=[self],
            named_arguments={
                "list_filters": list_filters,
                "list_generators": list_generators,
                "filter": filter,
                "output_rect": output_rect,
            },
        )[0]

    def corr(self, reference_stream: "Stream") -> "Stream":
        """Calculate the correlation between two video streams.

        Args:
            reference_stream (Stream): Input video stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="corr", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def cover_rect(
        self,
        cover: str | None = None,
        mode: Literal["cover", "blur"] | int | None = None,
    ) -> "Stream":
        """Find and cover a user specified object.

        Args:
            cover (str): cover bitmap filename

            mode (int | str): set removal mode (from 0 to 1)

                Allowed values:
                    * cover: cover area with bitmap
                    * blur: blur area

                Defaults to blur.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="cover_rect",
            inputs=[self],
            named_arguments={
                "cover": cover,
                "mode": mode,
            },
        )[0]

    def crop(
        self,
        out_w: str | None = None,
        w: str | None = None,
        out_h: str | None = None,
        h: str | None = None,
        x: str | None = None,
        y: str | None = None,
        keep_aspect: bool | None = None,
        exact: bool | None = None,
    ) -> "Stream":
        """Crop the input video.

        Args:
            out_w (str): set the width crop area expression

                Defaults to iw.
            w (str): set the width crop area expression

                Defaults to iw.
            out_h (str): set the height crop area expression

                Defaults to ih.
            h (str): set the height crop area expression

                Defaults to ih.
            x (str): set the x crop area expression

                Defaults to (in_w-out_w)/2.
            y (str): set the y crop area expression

                Defaults to (in_h-out_h)/2.
            keep_aspect (bool): keep aspect ratio

                Defaults to false.
            exact (bool): do exact cropping

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="crop",
            inputs=[self],
            named_arguments={
                "out_w": out_w,
                "w": w,
                "out_h": out_h,
                "h": h,
                "x": x,
                "y": y,
                "keep_aspect": keep_aspect,
                "exact": exact,
            },
        )[0]

    def cropdetect(
        self,
        limit: float | None = None,
        round: int | None = None,
        reset: int | None = None,
        skip: int | None = None,
        reset_count: int | None = None,
        max_outliers: int | None = None,
        mode: Literal["black", "mvedges"] | int | None = None,
        high: float | None = None,
        low: float | None = None,
        mv_threshold: int | None = None,
    ) -> "Stream":
        """Auto-detect crop size.

        Args:
            limit (float): Threshold below which the pixel is considered black (from 0 to 65535)

                Defaults to 0.0941176.
            round (int): Value by which the width/height should be divisible (from 0 to INT_MAX)

                Defaults to 16.
            reset (int): Recalculate the crop area after this many frames (from 0 to INT_MAX)

                Defaults to 0.
            skip (int): Number of initial frames to skip (from 0 to INT_MAX)

                Defaults to 2.
            reset_count (int): Recalculate the crop area after this many frames (from 0 to INT_MAX)

                Defaults to 0.
            max_outliers (int): Threshold count of outliers (from 0 to INT_MAX)

                Defaults to 0.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * black: detect black pixels surrounding the video
                    * mvedges: detect motion and edged surrounding the video

                Defaults to black.
            high (float): Set high threshold for edge detection (from 0 to 1)

                Defaults to 0.0980392.
            low (float): Set low threshold for edge detection (from 0 to 1)

                Defaults to 0.0588235.
            mv_threshold (int): motion vector threshold when estimating video window size (from 0 to 100)

                Defaults to 8.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="cropdetect",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "round": round,
                "reset": reset,
                "skip": skip,
                "reset_count": reset_count,
                "max_outliers": max_outliers,
                "mode": mode,
                "high": high,
                "low": low,
                "mv_threshold": mv_threshold,
            },
        )[0]

    def crossfeed(
        self,
        strength: float | None = None,
        range: float | None = None,
        slope: float | None = None,
        level_in: float | None = None,
        level_out: float | None = None,
        block_size: int | None = None,
    ) -> "Stream":
        """Apply headphone crossfeed filter.

        Args:
            strength (float): set crossfeed strength (from 0 to 1)

                Defaults to 0.2.
            range (float): set soundstage wideness (from 0 to 1)

                Defaults to 0.5.
            slope (float): set curve slope (from 0.01 to 1)

                Defaults to 0.5.
            level_in (float): set level in (from 0 to 1)

                Defaults to 0.9.
            level_out (float): set level out (from 0 to 1)

                Defaults to 1.
            block_size (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="crossfeed",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "range": range,
                "slope": slope,
                "level_in": level_in,
                "level_out": level_out,
                "block_size": block_size,
            },
        )[0]

    def crystalizer(self, i: float | None = None, c: bool | None = None) -> "Stream":
        """Simple audio noise sharpening filter.

        Args:
            i (float): set intensity (from -10 to 10)

                Defaults to 2.
            c (bool): enable clipping

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="crystalizer",
            inputs=[self],
            named_arguments={
                "i": i,
                "c": c,
            },
        )[0]

    def cue(
        self,
        cue: str | None = None,
        preroll: str | None = None,
        buffer: str | None = None,
    ) -> "Stream":
        """Delay filtering to match a cue.

        Args:
            cue (str): cue unix timestamp in microseconds (from 0 to I64_MAX)

                Defaults to 0.
            preroll (str): preroll duration in seconds

                Defaults to 0.
            buffer (str): buffer duration in seconds

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="cue",
            inputs=[self],
            named_arguments={
                "cue": cue,
                "preroll": preroll,
                "buffer": buffer,
            },
        )[0]

    def curves(
        self,
        preset: Literal[
            "none",
            "color_negative",
            "cross_process",
            "darker",
            "increase_contrast",
            "lighter",
            "linear_contrast",
            "medium_contrast",
            "negative",
            "strong_contrast",
            "vintage",
        ]
        | int
        | None = None,
        master: str | None = None,
        m: str | None = None,
        red: str | None = None,
        r: str | None = None,
        green: str | None = None,
        g: str | None = None,
        blue: str | None = None,
        b: str | None = None,
        all: str | None = None,
        psfile: str | None = None,
        plot: str | None = None,
        interp: Literal["natural", "pchip"] | int | None = None,
    ) -> "Stream":
        """Adjust components curves.

        Args:
            preset (int | str): select a color curves preset (from 0 to 10)

                Allowed values:
                    * none
                    * color_negative
                    * cross_process
                    * darker
                    * increase_contrast
                    * lighter
                    * linear_contrast
                    * medium_contrast
                    * negative
                    * strong_contrast
                    * vintage

                Defaults to none.
            master (str): set master points coordinates

            m (str): set master points coordinates

            red (str): set red points coordinates

            r (str): set red points coordinates

            green (str): set green points coordinates

            g (str): set green points coordinates

            blue (str): set blue points coordinates

            b (str): set blue points coordinates

            all (str): set points coordinates for all components

            psfile (str): set Photoshop curves file name

            plot (str): save Gnuplot script of the curves in specified file

            interp (int | str): specify the kind of interpolation (from 0 to 1)

                Allowed values:
                    * natural: natural cubic spline
                    * pchip: monotonically cubic interpolation

                Defaults to natural.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="curves",
            inputs=[self],
            named_arguments={
                "preset": preset,
                "master": master,
                "m": m,
                "red": red,
                "r": r,
                "green": green,
                "g": g,
                "blue": blue,
                "b": b,
                "all": all,
                "psfile": psfile,
                "plot": plot,
                "interp": interp,
            },
        )[0]

    def datascope(
        self,
        size: str | None = None,
        s: str | None = None,
        x: int | None = None,
        y: int | None = None,
        mode: Literal["mono", "color", "color2"] | int | None = None,
        axis: bool | None = None,
        opacity: float | None = None,
        format: Literal["hex", "dec"] | int | None = None,
        components: int | None = None,
    ) -> "Stream":
        """Video data analysis.

        Args:
            size (str): set output size

                Defaults to hd720.
            s (str): set output size

                Defaults to hd720.
            x (int): set x offset (from 0 to INT_MAX)

                Defaults to 0.
            y (int): set y offset (from 0 to INT_MAX)

                Defaults to 0.
            mode (int | str): set scope mode (from 0 to 2)

                Allowed values:
                    * mono
                    * color
                    * color2

                Defaults to mono.
            axis (bool): draw column/row numbers

                Defaults to false.
            opacity (float): set background opacity (from 0 to 1)

                Defaults to 0.75.
            format (int | str): set display number format (from 0 to 1)

                Allowed values:
                    * hex
                    * dec

                Defaults to hex.
            components (int): set components to display (from 1 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="datascope",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "x": x,
                "y": y,
                "mode": mode,
                "axis": axis,
                "opacity": opacity,
                "format": format,
                "components": components,
            },
        )[0]

    def dblur(
        self,
        angle: float | None = None,
        radius: float | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply Directional Blur filter.

        Args:
            angle (float): set angle (from 0 to 360)

                Defaults to 45.
            radius (float): set radius (from 0 to 8192)

                Defaults to 5.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dblur",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "radius": radius,
                "planes": planes,
            },
        )[0]

    def dcshift(
        self, shift: float | None = None, limitergain: float | None = None
    ) -> "Stream":
        """Apply a DC shift to the audio.

        Args:
            shift (float): set DC shift (from -1 to 1)

                Defaults to 0.
            limitergain (float): set limiter gain (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dcshift",
            inputs=[self],
            named_arguments={
                "shift": shift,
                "limitergain": limitergain,
            },
        )[0]

    def dctdnoiz(
        self,
        sigma: float | None = None,
        s: float | None = None,
        overlap: int | None = None,
        expr: str | None = None,
        e: str | None = None,
        n: int | None = None,
    ) -> "Stream":
        """Denoise frames using 2D DCT.

        Args:
            sigma (float): set noise sigma constant (from 0 to 999)

                Defaults to 0.
            s (float): set noise sigma constant (from 0 to 999)

                Defaults to 0.
            overlap (int): set number of block overlapping pixels (from -1 to 15)

                Defaults to -1.
            expr (str): set coefficient factor expression

            e (str): set coefficient factor expression

            n (int): set the block size, expressed in bits (from 3 to 4)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dctdnoiz",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "s": s,
                "overlap": overlap,
                "expr": expr,
                "e": e,
                "n": n,
            },
        )[0]

    def deband(
        self,
        _1thr: float | None = None,
        _2thr: float | None = None,
        _3thr: float | None = None,
        _4thr: float | None = None,
        range: int | None = None,
        r: int | None = None,
        direction: float | None = None,
        d: float | None = None,
        blur: bool | None = None,
        b: bool | None = None,
        coupling: bool | None = None,
        c: bool | None = None,
    ) -> "Stream":
        """Debands video.

        Args:
            _1thr (float): set 1st plane threshold (from 3e-05 to 0.5)

                Defaults to 0.02.
            _2thr (float): set 2nd plane threshold (from 3e-05 to 0.5)

                Defaults to 0.02.
            _3thr (float): set 3rd plane threshold (from 3e-05 to 0.5)

                Defaults to 0.02.
            _4thr (float): set 4th plane threshold (from 3e-05 to 0.5)

                Defaults to 0.02.
            range (int): set range (from INT_MIN to INT_MAX)

                Defaults to 16.
            r (int): set range (from INT_MIN to INT_MAX)

                Defaults to 16.
            direction (float): set direction (from -6.28319 to 6.28319)

                Defaults to 6.28319.
            d (float): set direction (from -6.28319 to 6.28319)

                Defaults to 6.28319.
            blur (bool): set blur

                Defaults to true.
            b (bool): set blur

                Defaults to true.
            coupling (bool): set plane coupling

                Defaults to false.
            c (bool): set plane coupling

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deband",
            inputs=[self],
            named_arguments={
                "1thr": _1thr,
                "2thr": _2thr,
                "3thr": _3thr,
                "4thr": _4thr,
                "range": range,
                "r": r,
                "direction": direction,
                "d": d,
                "blur": blur,
                "b": b,
                "coupling": coupling,
                "c": c,
            },
        )[0]

    def deblock(
        self,
        filter: Literal["weak", "strong"] | int | None = None,
        block: int | None = None,
        alpha: float | None = None,
        beta: float | None = None,
        gamma: float | None = None,
        delta: float | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Deblock video.

        Args:
            filter (int | str): set type of filter (from 0 to 1)

                Allowed values:
                    * weak
                    * strong

                Defaults to strong.
            block (int): set size of block (from 4 to 512)

                Defaults to 8.
            alpha (float): set 1st detection threshold (from 0 to 1)

                Defaults to 0.098.
            beta (float): set 2nd detection threshold (from 0 to 1)

                Defaults to 0.05.
            gamma (float): set 3rd detection threshold (from 0 to 1)

                Defaults to 0.05.
            delta (float): set 4th detection threshold (from 0 to 1)

                Defaults to 0.05.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deblock",
            inputs=[self],
            named_arguments={
                "filter": filter,
                "block": block,
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
                "delta": delta,
                "planes": planes,
            },
        )[0]

    def decimate(
        self,
        *streams: "Stream",
        cycle: int | None = None,
        dupthresh: float | None = None,
        scthresh: float | None = None,
        blockx: int | None = None,
        blocky: int | None = None,
        ppsrc: bool | None = None,
        chroma: bool | None = None,
        mixed: bool | None = None,
    ) -> "Stream":
        """Decimate frames (post field matching filter).

        Args:
            *streams (Stream): One or more input streams.
            cycle (int): set the number of frame from which one will be dropped (from 2 to 25)

                Defaults to 5.
            dupthresh (float): set duplicate threshold (from 0 to 100)

                Defaults to 1.1.
            scthresh (float): set scene change threshold (from 0 to 100)

                Defaults to 15.
            blockx (int): set the size of the x-axis blocks used during metric calculations (from 4 to 512)

                Defaults to 32.
            blocky (int): set the size of the y-axis blocks used during metric calculations (from 4 to 512)

                Defaults to 32.
            ppsrc (bool): mark main input as a pre-processed input and activate clean source input stream

                Defaults to false.
            chroma (bool): set whether or not chroma is considered in the metric calculations

                Defaults to true.
            mixed (bool): set whether or not the input only partially contains content to be decimated

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="decimate",
            inputs=[self, *streams],
            named_arguments={
                "cycle": cycle,
                "dupthresh": dupthresh,
                "scthresh": scthresh,
                "blockx": blockx,
                "blocky": blocky,
                "ppsrc": ppsrc,
                "chroma": chroma,
                "mixed": mixed,
            },
        )[0]

    def deconvolve(
        self,
        impulse_stream: "Stream",
        planes: int | None = None,
        impulse: Literal["first", "all"] | int | None = None,
        noise: float | None = None,
    ) -> "Stream":
        """Deconvolve first video stream with second video stream.

        Args:
            impulse_stream (Stream): Input video stream.
            planes (int): set planes to deconvolve (from 0 to 15)

                Defaults to 7.
            impulse (int | str): when to process impulses (from 0 to 1)

                Allowed values:
                    * first: process only first impulse, ignore rest
                    * all: process all impulses

                Defaults to all.
            noise (float): set noise (from 0 to 1)

                Defaults to 1e-07.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deconvolve",
            inputs=[self, impulse_stream],
            named_arguments={
                "planes": planes,
                "impulse": impulse,
                "noise": noise,
            },
        )[0]

    def dedot(
        self,
        m: Literal["dotcrawl", "rainbows"] | None = None,
        lt: float | None = None,
        tl: float | None = None,
        tc: float | None = None,
        ct: float | None = None,
    ) -> "Stream":
        """Reduce cross-luminance and cross-color.

        Args:
            m (str): set filtering mode

                Allowed values:
                    * dotcrawl
                    * rainbows

                Defaults to dotcrawl+rainbows.
            lt (float): set spatial luma threshold (from 0 to 1)

                Defaults to 0.079.
            tl (float): set tolerance for temporal luma (from 0 to 1)

                Defaults to 0.079.
            tc (float): set tolerance for chroma temporal variation (from 0 to 1)

                Defaults to 0.058.
            ct (float): set temporal chroma threshold (from 0 to 1)

                Defaults to 0.019.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dedot",
            inputs=[self],
            named_arguments={
                "m": m,
                "lt": lt,
                "tl": tl,
                "tc": tc,
                "ct": ct,
            },
        )[0]

    def deesser(
        self,
        i: float | None = None,
        m: float | None = None,
        f: float | None = None,
        s: Literal["i", "o", "e"] | int | None = None,
    ) -> "Stream":
        """Apply de-essing to the audio.

        Args:
            i (float): set intensity (from 0 to 1)

                Defaults to 0.
            m (float): set max deessing (from 0 to 1)

                Defaults to 0.5.
            f (float): set frequency (from 0 to 1)

                Defaults to 0.5.
            s (int | str): set output mode (from 0 to 2)

                Allowed values:
                    * i: input
                    * o: output
                    * e: ess

                Defaults to o.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deesser",
            inputs=[self],
            named_arguments={
                "i": i,
                "m": m,
                "f": f,
                "s": s,
            },
        )[0]

    def deflate(
        self,
        threshold0: int | None = None,
        threshold1: int | None = None,
        threshold2: int | None = None,
        threshold3: int | None = None,
    ) -> "Stream":
        """Apply deflate effect.

        Args:
            threshold0 (int): set threshold for 1st plane (from 0 to 65535)

                Defaults to 65535.
            threshold1 (int): set threshold for 2nd plane (from 0 to 65535)

                Defaults to 65535.
            threshold2 (int): set threshold for 3rd plane (from 0 to 65535)

                Defaults to 65535.
            threshold3 (int): set threshold for 4th plane (from 0 to 65535)

                Defaults to 65535.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deflate",
            inputs=[self],
            named_arguments={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def deflicker(
        self,
        size: int | None = None,
        s: int | None = None,
        mode: Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | int | None = None,
        m: Literal["am", "gm", "hm", "qm", "cm", "pm", "median"] | int | None = None,
        bypass: bool | None = None,
    ) -> "Stream":
        """Remove temporal frame luminance variations.

        Args:
            size (int): set how many frames to use (from 2 to 129)

                Defaults to 5.
            s (int): set how many frames to use (from 2 to 129)

                Defaults to 5.
            mode (int | str): set how to smooth luminance (from 0 to 6)

                Allowed values:
                    * am: arithmetic mean
                    * gm: geometric mean
                    * hm: harmonic mean
                    * qm: quadratic mean
                    * cm: cubic mean
                    * pm: power mean
                    * median: median

                Defaults to am.
            m (int | str): set how to smooth luminance (from 0 to 6)

                Allowed values:
                    * am: arithmetic mean
                    * gm: geometric mean
                    * hm: harmonic mean
                    * qm: quadratic mean
                    * cm: cubic mean
                    * pm: power mean
                    * median: median

                Defaults to am.
            bypass (bool): leave frames unchanged

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deflicker",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "m": m,
                "bypass": bypass,
            },
        )[0]

    def dejudder(self, cycle: int | None = None) -> "Stream":
        """Remove judder produced by pullup.

        Args:
            cycle (int): set the length of the cycle to use for dejuddering (from 2 to 240)

                Defaults to 4.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dejudder",
            inputs=[self],
            named_arguments={
                "cycle": cycle,
            },
        )[0]

    def delogo(
        self,
        x: str | None = None,
        y: str | None = None,
        w: str | None = None,
        h: str | None = None,
        show: bool | None = None,
    ) -> "Stream":
        """Remove logo from input video.

        Args:
            x (str): set logo x position

                Defaults to -1.
            y (str): set logo y position

                Defaults to -1.
            w (str): set logo width

                Defaults to -1.
            h (str): set logo height

                Defaults to -1.
            show (bool): show delogo area

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="delogo",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "show": show,
            },
        )[0]

    def deshake(
        self,
        x: int | None = None,
        y: int | None = None,
        w: int | None = None,
        h: int | None = None,
        rx: int | None = None,
        ry: int | None = None,
        edge: Literal["blank", "original", "clamp", "mirror"] | int | None = None,
        blocksize: int | None = None,
        contrast: int | None = None,
        search: Literal["exhaustive", "less"] | int | None = None,
        filename: str | None = None,
        opencl: bool | None = None,
    ) -> "Stream":
        """Stabilize shaky video.

        Args:
            x (int): set x for the rectangular search area (from -1 to INT_MAX)

                Defaults to -1.
            y (int): set y for the rectangular search area (from -1 to INT_MAX)

                Defaults to -1.
            w (int): set width for the rectangular search area (from -1 to INT_MAX)

                Defaults to -1.
            h (int): set height for the rectangular search area (from -1 to INT_MAX)

                Defaults to -1.
            rx (int): set x for the rectangular search area (from 0 to 64)

                Defaults to 16.
            ry (int): set y for the rectangular search area (from 0 to 64)

                Defaults to 16.
            edge (int | str): set edge mode (from 0 to 3)

                Allowed values:
                    * blank: fill zeroes at blank locations
                    * original: original image at blank locations
                    * clamp: extruded edge value at blank locations
                    * mirror: mirrored edge at blank locations

                Defaults to mirror.
            blocksize (int): set motion search blocksize (from 4 to 128)

                Defaults to 8.
            contrast (int): set contrast threshold for blocks (from 1 to 255)

                Defaults to 125.
            search (int | str): set search strategy (from 0 to 1)

                Allowed values:
                    * exhaustive: exhaustive search
                    * less: less exhaustive search

                Defaults to exhaustive.
            filename (str): set motion search detailed log file name

            opencl (bool): ignored

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="deshake",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "rx": rx,
                "ry": ry,
                "edge": edge,
                "blocksize": blocksize,
                "contrast": contrast,
                "search": search,
                "filename": filename,
                "opencl": opencl,
            },
        )[0]

    def despill(
        self,
        type: Literal["green", "blue"] | int | None = None,
        mix: float | None = None,
        expand: float | None = None,
        red: float | None = None,
        green: float | None = None,
        blue: float | None = None,
        brightness: float | None = None,
        alpha: bool | None = None,
    ) -> "Stream":
        """Despill video.

        Args:
            type (int | str): set the screen type (from 0 to 1)

                Allowed values:
                    * green: greenscreen
                    * blue: bluescreen

                Defaults to green.
            mix (float): set the spillmap mix (from 0 to 1)

                Defaults to 0.5.
            expand (float): set the spillmap expand (from 0 to 1)

                Defaults to 0.
            red (float): set red scale (from -100 to 100)

                Defaults to 0.
            green (float): set green scale (from -100 to 100)

                Defaults to -1.
            blue (float): set blue scale (from -100 to 100)

                Defaults to 0.
            brightness (float): set brightness (from -10 to 10)

                Defaults to 0.
            alpha (bool): change alpha component

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="despill",
            inputs=[self],
            named_arguments={
                "type": type,
                "mix": mix,
                "expand": expand,
                "red": red,
                "green": green,
                "blue": blue,
                "brightness": brightness,
                "alpha": alpha,
            },
        )[0]

    def detelecine(
        self,
        first_field: Literal["top", "t", "bottom", "b"] | int | None = None,
        pattern: str | None = None,
        start_frame: int | None = None,
    ) -> "Stream":
        """Apply an inverse telecine pattern.

        Args:
            first_field (int | str): select first field (from 0 to 1)

                Allowed values:
                    * top: select top field first
                    * t: select top field first
                    * bottom: select bottom field first
                    * b: select bottom field first

                Defaults to top.
            pattern (str): pattern that describe for how many fields a frame is to be displayed

                Defaults to 23.
            start_frame (int): position of first frame with respect to the pattern if stream is cut (from 0 to 13)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="detelecine",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
                "pattern": pattern,
                "start_frame": start_frame,
            },
        )[0]

    def dialoguenhance(
        self,
        original: float | None = None,
        enhance: float | None = None,
        voice: float | None = None,
    ) -> "Stream":
        """Audio Dialogue Enhancement.

        Args:
            original (float): set original center factor (from 0 to 1)

                Defaults to 1.
            enhance (float): set dialogue enhance factor (from 0 to 3)

                Defaults to 1.
            voice (float): set voice detection factor (from 2 to 32)

                Defaults to 2.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dialoguenhance",
            inputs=[self],
            named_arguments={
                "original": original,
                "enhance": enhance,
                "voice": voice,
            },
        )[0]

    def dilation(
        self,
        coordinates: int | None = None,
        threshold0: int | None = None,
        threshold1: int | None = None,
        threshold2: int | None = None,
        threshold3: int | None = None,
    ) -> "Stream":
        """Apply dilation effect.

        Args:
            coordinates (int): set coordinates (from 0 to 255)

                Defaults to 255.
            threshold0 (int): set threshold for 1st plane (from 0 to 65535)

                Defaults to 65535.
            threshold1 (int): set threshold for 2nd plane (from 0 to 65535)

                Defaults to 65535.
            threshold2 (int): set threshold for 3rd plane (from 0 to 65535)

                Defaults to 65535.
            threshold3 (int): set threshold for 4th plane (from 0 to 65535)

                Defaults to 65535.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dilation",
            inputs=[self],
            named_arguments={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def displace(
        self,
        xmap_stream: "Stream",
        ymap_stream: "Stream",
        edge: Literal["blank", "smear", "wrap", "mirror"] | int | None = None,
    ) -> "Stream":
        """Displace pixels.

        Args:
            xmap_stream (Stream): Input video stream.
            ymap_stream (Stream): Input video stream.
            edge (int | str): set edge mode (from 0 to 3)

                Allowed values:
                    * blank
                    * smear
                    * wrap
                    * mirror

                Defaults to smear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="displace",
            inputs=[self, xmap_stream, ymap_stream],
            named_arguments={
                "edge": edge,
            },
        )[0]

    def doubleweave(
        self, first_field: Literal["top", "t", "bottom", "b"] | int | None = None
    ) -> "Stream":
        """Weave input video fields into double number of frames.

        Args:
            first_field (int | str): set first field (from 0 to 1)

                Allowed values:
                    * top: set top field first
                    * t: set top field first
                    * bottom: set bottom field first
                    * b: set bottom field first

                Defaults to top.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="doubleweave",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
            },
        )[0]

    def drawbox(
        self,
        x: str | None = None,
        y: str | None = None,
        width: str | None = None,
        w: str | None = None,
        height: str | None = None,
        h: str | None = None,
        color: str | None = None,
        c: str | None = None,
        thickness: str | None = None,
        t: str | None = None,
        replace: bool | None = None,
        box_source: str | None = None,
    ) -> "Stream":
        """Draw a colored box on the input video.

        Args:
            x (str): set horizontal position of the left box edge

                Defaults to 0.
            y (str): set vertical position of the top box edge

                Defaults to 0.
            width (str): set width of the box

                Defaults to 0.
            w (str): set width of the box

                Defaults to 0.
            height (str): set height of the box

                Defaults to 0.
            h (str): set height of the box

                Defaults to 0.
            color (str): set color of the box

                Defaults to black.
            c (str): set color of the box

                Defaults to black.
            thickness (str): set the box thickness

                Defaults to 3.
            t (str): set the box thickness

                Defaults to 3.
            replace (bool): replace color & alpha

                Defaults to false.
            box_source (str): use data from bounding box in side data


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="drawbox",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "color": color,
                "c": c,
                "thickness": thickness,
                "t": t,
                "replace": replace,
                "box_source": box_source,
            },
        )[0]

    def drawgraph(
        self,
        m1: str | None = None,
        fg1: str | None = None,
        m2: str | None = None,
        fg2: str | None = None,
        m3: str | None = None,
        fg3: str | None = None,
        m4: str | None = None,
        fg4: str | None = None,
        bg: str | None = None,
        min: float | None = None,
        max: float | None = None,
        mode: Literal["bar", "dot", "line"] | int | None = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | int
        | None = None,
        size: str | None = None,
        s: str | None = None,
        rate: str | None = None,
        r: str | None = None,
    ) -> "Stream":
        """Draw a graph using input video metadata.

        Args:
            m1 (str): set 1st metadata key

            fg1 (str): set 1st foreground color expression

                Defaults to 0xffff0000.
            m2 (str): set 2nd metadata key

            fg2 (str): set 2nd foreground color expression

                Defaults to 0xff00ff00.
            m3 (str): set 3rd metadata key

            fg3 (str): set 3rd foreground color expression

                Defaults to 0xffff00ff.
            m4 (str): set 4th metadata key

            fg4 (str): set 4th foreground color expression

                Defaults to 0xffffff00.
            bg (str): set background color

                Defaults to white.
            min (float): set minimal value (from INT_MIN to INT_MAX)

                Defaults to -1.
            max (float): set maximal value (from INT_MIN to INT_MAX)

                Defaults to 1.
            mode (int | str): set graph mode (from 0 to 2)

                Allowed values:
                    * bar: draw bars
                    * dot: draw dots
                    * line: draw lines

                Defaults to line.
            slide (int | str): set slide mode (from 0 to 4)

                Allowed values:
                    * frame: draw new frames
                    * replace: replace old columns with new
                    * scroll: scroll from right to left
                    * rscroll: scroll from left to right
                    * picture: display graph in single frame

                Defaults to frame.
            size (str): set graph size

                Defaults to 900x256.
            s (str): set graph size

                Defaults to 900x256.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="drawgraph",
            inputs=[self],
            named_arguments={
                "m1": m1,
                "fg1": fg1,
                "m2": m2,
                "fg2": fg2,
                "m3": m3,
                "fg3": fg3,
                "m4": m4,
                "fg4": fg4,
                "bg": bg,
                "min": min,
                "max": max,
                "mode": mode,
                "slide": slide,
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
            },
        )[0]

    def drawgrid(
        self,
        x: str | None = None,
        y: str | None = None,
        width: str | None = None,
        w: str | None = None,
        height: str | None = None,
        h: str | None = None,
        color: str | None = None,
        c: str | None = None,
        thickness: str | None = None,
        t: str | None = None,
        replace: bool | None = None,
    ) -> "Stream":
        """Draw a colored grid on the input video.

        Args:
            x (str): set horizontal offset

                Defaults to 0.
            y (str): set vertical offset

                Defaults to 0.
            width (str): set width of grid cell

                Defaults to 0.
            w (str): set width of grid cell

                Defaults to 0.
            height (str): set height of grid cell

                Defaults to 0.
            h (str): set height of grid cell

                Defaults to 0.
            color (str): set color of the grid

                Defaults to black.
            c (str): set color of the grid

                Defaults to black.
            thickness (str): set grid line thickness

                Defaults to 1.
            t (str): set grid line thickness

                Defaults to 1.
            replace (bool): replace color & alpha

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="drawgrid",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "color": color,
                "c": c,
                "thickness": thickness,
                "t": t,
                "replace": replace,
            },
        )[0]

    def drawtext(
        self,
        fontfile: str | None = None,
        text: str | None = None,
        textfile: str | None = None,
        fontcolor: str | None = None,
        fontcolor_expr: str | None = None,
        boxcolor: str | None = None,
        bordercolor: str | None = None,
        shadowcolor: str | None = None,
        box: bool | None = None,
        boxborderw: str | None = None,
        line_spacing: int | None = None,
        fontsize: str | None = None,
        text_align: Literal[
            "left",
            "L",
            "right",
            "R",
            "center",
            "C",
            "top",
            "T",
            "bottom",
            "B",
            "middle",
            "M",
        ]
        | None = None,
        x: str | None = None,
        y: str | None = None,
        boxw: int | None = None,
        boxh: int | None = None,
        shadowx: int | None = None,
        shadowy: int | None = None,
        borderw: int | None = None,
        tabsize: int | None = None,
        basetime: str | None = None,
        font: str | None = None,
        expansion: Literal["none", "normal", "strftime"] | int | None = None,
        y_align: Literal["text", "baseline", "font"] | int | None = None,
        timecode: str | None = None,
        tc24hmax: bool | None = None,
        timecode_rate: str | None = None,
        r: str | None = None,
        rate: str | None = None,
        reload: int | None = None,
        alpha: str | None = None,
        fix_bounds: bool | None = None,
        start_number: int | None = None,
        text_source: str | None = None,
        ft_load_flags: Literal[
            "default",
            "no_scale",
            "no_hinting",
            "render",
            "no_bitmap",
            "vertical_layout",
            "force_autohint",
            "crop_bitmap",
            "pedantic",
            "ignore_global_advance_width",
            "no_recurse",
            "ignore_transform",
            "monochrome",
            "linear_design",
            "no_autohint",
        ]
        | None = None,
    ) -> "Stream":
        """Draw text on top of video frames using libfreetype library.

        Args:
            fontfile (str): set font file

            text (str): set text

            textfile (str): set text file

            fontcolor (str): set foreground color

                Defaults to black.
            fontcolor_expr (str): set foreground color expression

            boxcolor (str): set box color

                Defaults to white.
            bordercolor (str): set border color

                Defaults to black.
            shadowcolor (str): set shadow color

                Defaults to black.
            box (bool): set box

                Defaults to false.
            boxborderw (str): set box borders width

                Defaults to 0.
            line_spacing (int): set line spacing in pixels (from INT_MIN to INT_MAX)

                Defaults to 0.
            fontsize (str): set font size

            text_align (str): set text alignment

                Allowed values:
                    * left
                    * L
                    * right
                    * R
                    * center
                    * C
                    * top
                    * T
                    * bottom
                    * B
                    * middle
                    * M

                Defaults to 0.
            x (str): set x expression

                Defaults to 0.
            y (str): set y expression

                Defaults to 0.
            boxw (int): set box width (from 0 to INT_MAX)

                Defaults to 0.
            boxh (int): set box height (from 0 to INT_MAX)

                Defaults to 0.
            shadowx (int): set shadow x offset (from INT_MIN to INT_MAX)

                Defaults to 0.
            shadowy (int): set shadow y offset (from INT_MIN to INT_MAX)

                Defaults to 0.
            borderw (int): set border width (from INT_MIN to INT_MAX)

                Defaults to 0.
            tabsize (int): set tab size (from 0 to INT_MAX)

                Defaults to 4.
            basetime (str): set base time (from I64_MIN to I64_MAX)

                Defaults to I64_MIN.
            font (str): Font name

                Defaults to Sans.
            expansion (int | str): set the expansion mode (from 0 to 2)

                Allowed values:
                    * none: set no expansion
                    * normal: set normal expansion
                    * strftime: set strftime expansion (deprecated)

                Defaults to normal.
            y_align (int | str): set the y alignment (from 0 to 2)

                Allowed values:
                    * text: y is referred to the top of the first text line
                    * baseline: y is referred to the baseline of the first line
                    * font: y is referred to the font defined line metrics

                Defaults to text.
            timecode (str): set initial timecode

            tc24hmax (bool): set 24 hours max (timecode only)

                Defaults to false.
            timecode_rate (str): set rate (timecode only) (from 0 to INT_MAX)

                Defaults to 0/1.
            r (str): set rate (timecode only) (from 0 to INT_MAX)

                Defaults to 0/1.
            rate (str): set rate (timecode only) (from 0 to INT_MAX)

                Defaults to 0/1.
            reload (int): reload text file at specified frame interval (from 0 to INT_MAX)

                Defaults to 0.
            alpha (str): apply alpha while rendering

                Defaults to 1.
            fix_bounds (bool): check and fix text coords to avoid clipping

                Defaults to false.
            start_number (int): start frame number for n/frame_num variable (from 0 to INT_MAX)

                Defaults to 0.
            text_source (str): the source of text

            ft_load_flags (str): set font loading flags for libfreetype

                Allowed values:
                    * default
                    * no_scale
                    * no_hinting
                    * render
                    * no_bitmap
                    * vertical_layout
                    * force_autohint
                    * crop_bitmap
                    * pedantic
                    * ignore_global_advance_width
                    * no_recurse
                    * ignore_transform
                    * monochrome
                    * linear_design
                    * no_autohint

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="drawtext",
            inputs=[self],
            named_arguments={
                "fontfile": fontfile,
                "text": text,
                "textfile": textfile,
                "fontcolor": fontcolor,
                "fontcolor_expr": fontcolor_expr,
                "boxcolor": boxcolor,
                "bordercolor": bordercolor,
                "shadowcolor": shadowcolor,
                "box": box,
                "boxborderw": boxborderw,
                "line_spacing": line_spacing,
                "fontsize": fontsize,
                "text_align": text_align,
                "x": x,
                "y": y,
                "boxw": boxw,
                "boxh": boxh,
                "shadowx": shadowx,
                "shadowy": shadowy,
                "borderw": borderw,
                "tabsize": tabsize,
                "basetime": basetime,
                "font": font,
                "expansion": expansion,
                "y_align": y_align,
                "timecode": timecode,
                "tc24hmax": tc24hmax,
                "timecode_rate": timecode_rate,
                "r": r,
                "rate": rate,
                "reload": reload,
                "alpha": alpha,
                "fix_bounds": fix_bounds,
                "start_number": start_number,
                "text_source": text_source,
                "ft_load_flags": ft_load_flags,
            },
        )[0]

    def drmeter(self, length: float | None = None) -> "Stream":
        """Measure audio dynamic range.

        Args:
            length (float): set the window length (from 0.01 to 10)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="drmeter",
            inputs=[self],
            named_arguments={
                "length": length,
            },
        )[0]

    def dynaudnorm(
        self,
        framelen: int | None = None,
        f: int | None = None,
        gausssize: int | None = None,
        g: int | None = None,
        peak: float | None = None,
        p: float | None = None,
        maxgain: float | None = None,
        m: float | None = None,
        targetrms: float | None = None,
        r: float | None = None,
        coupling: bool | None = None,
        n: bool | None = None,
        correctdc: bool | None = None,
        c: bool | None = None,
        altboundary: bool | None = None,
        b: bool | None = None,
        compress: float | None = None,
        s: float | None = None,
        threshold: float | None = None,
        t: float | None = None,
        channels: str | None = None,
        h: str | None = None,
        overlap: float | None = None,
        o: float | None = None,
        curve: str | None = None,
        v: str | None = None,
    ) -> "Stream":
        """Dynamic Audio Normalizer.

        Args:
            framelen (int): set the frame length in msec (from 10 to 8000)

                Defaults to 500.
            f (int): set the frame length in msec (from 10 to 8000)

                Defaults to 500.
            gausssize (int): set the filter size (from 3 to 301)

                Defaults to 31.
            g (int): set the filter size (from 3 to 301)

                Defaults to 31.
            peak (float): set the peak value (from 0 to 1)

                Defaults to 0.95.
            p (float): set the peak value (from 0 to 1)

                Defaults to 0.95.
            maxgain (float): set the max amplification (from 1 to 100)

                Defaults to 10.
            m (float): set the max amplification (from 1 to 100)

                Defaults to 10.
            targetrms (float): set the target RMS (from 0 to 1)

                Defaults to 0.
            r (float): set the target RMS (from 0 to 1)

                Defaults to 0.
            coupling (bool): set channel coupling

                Defaults to true.
            n (bool): set channel coupling

                Defaults to true.
            correctdc (bool): set DC correction

                Defaults to false.
            c (bool): set DC correction

                Defaults to false.
            altboundary (bool): set alternative boundary mode

                Defaults to false.
            b (bool): set alternative boundary mode

                Defaults to false.
            compress (float): set the compress factor (from 0 to 30)

                Defaults to 0.
            s (float): set the compress factor (from 0 to 30)

                Defaults to 0.
            threshold (float): set the threshold value (from 0 to 1)

                Defaults to 0.
            t (float): set the threshold value (from 0 to 1)

                Defaults to 0.
            channels (str): set channels to filter

                Defaults to all.
            h (str): set channels to filter

                Defaults to all.
            overlap (float): set the frame overlap (from 0 to 1)

                Defaults to 0.
            o (float): set the frame overlap (from 0 to 1)

                Defaults to 0.
            curve (str): set the custom peak mapping curve

            v (str): set the custom peak mapping curve


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="dynaudnorm",
            inputs=[self],
            named_arguments={
                "framelen": framelen,
                "f": f,
                "gausssize": gausssize,
                "g": g,
                "peak": peak,
                "p": p,
                "maxgain": maxgain,
                "m": m,
                "targetrms": targetrms,
                "r": r,
                "coupling": coupling,
                "n": n,
                "correctdc": correctdc,
                "c": c,
                "altboundary": altboundary,
                "b": b,
                "compress": compress,
                "s": s,
                "threshold": threshold,
                "t": t,
                "channels": channels,
                "h": h,
                "overlap": overlap,
                "o": o,
                "curve": curve,
                "v": v,
            },
        )[0]

    def earwax(
        self,
    ) -> "Stream":
        """Widen the stereo image.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="earwax", inputs=[self], named_arguments={}
        )[0]

    def ebur128(
        self,
        video: bool | None = None,
        size: str | None = None,
        meter: int | None = None,
        framelog: Literal["quiet", "info", "verbose"] | int | None = None,
        metadata: bool | None = None,
        peak: Literal["none", "sample", "true"] | None = None,
        dualmono: bool | None = None,
        panlaw: float | None = None,
        target: int | None = None,
        gauge: Literal["momentary", "m", "shortterm", "s"] | int | None = None,
        scale: Literal["absolute", "LUFS", "relative", "LU"] | int | None = None,
        integrated: float | None = None,
        range: float | None = None,
        lra_low: float | None = None,
        lra_high: float | None = None,
        sample_peak: float | None = None,
        true_peak: float | None = None,
    ) -> "FilterMultiOutput":
        """EBU R128 scanner.

        Args:
            video (bool): set video output

                Defaults to false.
            size (str): set video size

                Defaults to 640x480.
            meter (int): set scale meter (+9 to +18) (from 9 to 18)

                Defaults to 9.
            framelog (int | str): force frame logging level (from INT_MIN to INT_MAX)

                Allowed values:
                    * quiet: logging disabled
                    * info: information logging level
                    * verbose: verbose logging level

                Defaults to -1.
            metadata (bool): inject metadata in the filtergraph

                Defaults to false.
            peak (str): set peak mode

                Allowed values:
                    * none: any peak mode
                    * sample: peak-sample mode
                    * true: true-peak mode

                Defaults to 0.
            dualmono (bool): treat mono input files as dual-mono

                Defaults to false.
            panlaw (float): set a specific pan law for dual-mono files (from -10 to 0)

                Defaults to -3.0103.
            target (int): set a specific target level in LUFS (-23 to 0) (from -23 to 0)

                Defaults to -23.
            gauge (int | str): set gauge display type (from 0 to 1)

                Allowed values:
                    * momentary: display momentary value
                    * m: display momentary value
                    * shortterm: display short-term value
                    * s: display short-term value

                Defaults to momentary.
            scale (int | str): sets display method for the stats (from 0 to 1)

                Allowed values:
                    * absolute: display absolute values (LUFS)
                    * LUFS: display absolute values (LUFS)
                    * relative: display values relative to target (LU)
                    * LU: display values relative to target (LU)

                Defaults to absolute.
            integrated (float): integrated loudness (LUFS) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.
            range (float): loudness range (LU) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.
            lra_low (float): LRA low (LUFS) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.
            lra_high (float): LRA high (LUFS) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.
            sample_peak (float): sample peak (dBFS) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.
            true_peak (float): true peak (dBFS) (from -DBL_MAX to DBL_MAX)

                Defaults to 0.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="ebur128",
            inputs=[self],
            named_arguments={
                "video": video,
                "size": size,
                "meter": meter,
                "framelog": framelog,
                "metadata": metadata,
                "peak": peak,
                "dualmono": dualmono,
                "panlaw": panlaw,
                "target": target,
                "gauge": gauge,
                "scale": scale,
                "integrated": integrated,
                "range": range,
                "lra_low": lra_low,
                "lra_high": lra_high,
                "sample_peak": sample_peak,
                "true_peak": true_peak,
            },
        )

    def edgedetect(
        self,
        high: float | None = None,
        low: float | None = None,
        mode: Literal["wires", "colormix", "canny"] | int | None = None,
        planes: Literal["y", "u", "v", "r", "g", "b"] | None = None,
    ) -> "Stream":
        """Detect and draw edge.

        Args:
            high (float): set high threshold (from 0 to 1)

                Defaults to 0.196078.
            low (float): set low threshold (from 0 to 1)

                Defaults to 0.0784314.
            mode (int | str): set mode (from 0 to 2)

                Allowed values:
                    * wires: white/gray wires on black
                    * colormix: mix colors
                    * canny: detect edges on planes

                Defaults to wires.
            planes (str): set planes to filter

                Allowed values:
                    * y: luma plane
                    * u: u plane
                    * v: v plane
                    * r: red plane
                    * g: green plane
                    * b: blue plane

                Defaults to y+u+v+r+g+b.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="edgedetect",
            inputs=[self],
            named_arguments={
                "high": high,
                "low": low,
                "mode": mode,
                "planes": planes,
            },
        )[0]

    def elbg(
        self,
        codebook_length: int | None = None,
        l: int | None = None,
        nb_steps: int | None = None,
        n: int | None = None,
        seed: str | None = None,
        s: str | None = None,
        pal8: bool | None = None,
        use_alpha: bool | None = None,
    ) -> "Stream":
        """Apply posterize effect, using the ELBG algorithm.

        Args:
            codebook_length (int): set codebook length (from 1 to INT_MAX)

                Defaults to 256.
            l (int): set codebook length (from 1 to INT_MAX)

                Defaults to 256.
            nb_steps (int): set max number of steps used to compute the mapping (from 1 to INT_MAX)

                Defaults to 1.
            n (int): set max number of steps used to compute the mapping (from 1 to INT_MAX)

                Defaults to 1.
            seed (str): set the random seed (from -1 to UINT32_MAX)

                Defaults to -1.
            s (str): set the random seed (from -1 to UINT32_MAX)

                Defaults to -1.
            pal8 (bool): set the pal8 output

                Defaults to false.
            use_alpha (bool): use alpha channel for mapping

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="elbg",
            inputs=[self],
            named_arguments={
                "codebook_length": codebook_length,
                "l": l,
                "nb_steps": nb_steps,
                "n": n,
                "seed": seed,
                "s": s,
                "pal8": pal8,
                "use_alpha": use_alpha,
            },
        )[0]

    def entropy(self, mode: Literal["normal", "diff"] | int | None = None) -> "Stream":
        """Measure video frames entropy.

        Args:
            mode (int | str): set kind of histogram entropy measurement (from 0 to 1)

                Allowed values:
                    * normal
                    * diff

                Defaults to normal.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="entropy",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def epx(self, n: int | None = None) -> "Stream":
        """Scale the input using EPX algorithm.

        Args:
            n (int): set scale factor (from 2 to 3)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="epx",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def eq(
        self,
        contrast: str | None = None,
        brightness: str | None = None,
        saturation: str | None = None,
        gamma: str | None = None,
        gamma_r: str | None = None,
        gamma_g: str | None = None,
        gamma_b: str | None = None,
        gamma_weight: str | None = None,
        eval: Literal["init", "frame"] | int | None = None,
    ) -> "Stream":
        """Adjust brightness, contrast, gamma, and saturation.

        Args:
            contrast (str): set the contrast adjustment, negative values give a negative image

                Defaults to 1.0.
            brightness (str): set the brightness adjustment

                Defaults to 0.0.
            saturation (str): set the saturation adjustment

                Defaults to 1.0.
            gamma (str): set the initial gamma value

                Defaults to 1.0.
            gamma_r (str): gamma value for red

                Defaults to 1.0.
            gamma_g (str): gamma value for green

                Defaults to 1.0.
            gamma_b (str): gamma value for blue

                Defaults to 1.0.
            gamma_weight (str): set the gamma weight which reduces the effect of gamma on bright areas

                Defaults to 1.0.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions per-frame

                Defaults to init.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="eq",
            inputs=[self],
            named_arguments={
                "contrast": contrast,
                "brightness": brightness,
                "saturation": saturation,
                "gamma": gamma,
                "gamma_r": gamma_r,
                "gamma_g": gamma_g,
                "gamma_b": gamma_b,
                "gamma_weight": gamma_weight,
                "eval": eval,
            },
        )[0]

    def equalizer(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply two-pole peaking equalization (EQ) filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 0.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 0.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 1.
            w (float): set width (from 0 to 99999)

                Defaults to 1.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="equalizer",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def erosion(
        self,
        coordinates: int | None = None,
        threshold0: int | None = None,
        threshold1: int | None = None,
        threshold2: int | None = None,
        threshold3: int | None = None,
    ) -> "Stream":
        """Apply erosion effect.

        Args:
            coordinates (int): set coordinates (from 0 to 255)

                Defaults to 255.
            threshold0 (int): set threshold for 1st plane (from 0 to 65535)

                Defaults to 65535.
            threshold1 (int): set threshold for 2nd plane (from 0 to 65535)

                Defaults to 65535.
            threshold2 (int): set threshold for 3rd plane (from 0 to 65535)

                Defaults to 65535.
            threshold3 (int): set threshold for 4th plane (from 0 to 65535)

                Defaults to 65535.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="erosion",
            inputs=[self],
            named_arguments={
                "coordinates": coordinates,
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def estdif(
        self,
        mode: Literal["frame", "field"] | int | None = None,
        parity: Literal["tff", "bff", "auto"] | int | None = None,
        deint: Literal["all", "interlaced"] | int | None = None,
        rslope: int | None = None,
        redge: int | None = None,
        ecost: int | None = None,
        mcost: int | None = None,
        dcost: int | None = None,
        interp: Literal["2p", "4p", "6p"] | int | None = None,
    ) -> "Stream":
        """Apply Edge Slope Tracing deinterlace.

        Args:
            mode (int | str): specify the mode (from 0 to 1)

                Allowed values:
                    * frame: send one frame for each frame
                    * field: send one frame for each field

                Defaults to field.
            parity (int | str): specify the assumed picture field parity (from -1 to 1)

                Allowed values:
                    * tff: assume top field first
                    * bff: assume bottom field first
                    * auto: auto detect parity

                Defaults to auto.
            deint (int | str): specify which frames to deinterlace (from 0 to 1)

                Allowed values:
                    * all: deinterlace all frames
                    * interlaced: only deinterlace frames marked as interlaced

                Defaults to all.
            rslope (int): specify the search radius for edge slope tracing (from 1 to 15)

                Defaults to 1.
            redge (int): specify the search radius for best edge matching (from 0 to 15)

                Defaults to 2.
            ecost (int): specify the edge cost for edge matching (from 0 to 50)

                Defaults to 2.
            mcost (int): specify the middle cost for edge matching (from 0 to 50)

                Defaults to 1.
            dcost (int): specify the distance cost for edge matching (from 0 to 50)

                Defaults to 1.
            interp (int | str): specify the type of interpolation (from 0 to 2)

                Allowed values:
                    * 2p: two-point interpolation
                    * 4p: four-point interpolation
                    * 6p: six-point interpolation

                Defaults to 4p.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="estdif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
                "rslope": rslope,
                "redge": redge,
                "ecost": ecost,
                "mcost": mcost,
                "dcost": dcost,
                "interp": interp,
            },
        )[0]

    def exposure(
        self, exposure: float | None = None, black: float | None = None
    ) -> "Stream":
        """Adjust exposure of the video stream.

        Args:
            exposure (float): set the exposure correction (from -3 to 3)

                Defaults to 0.
            black (float): set the black level correction (from -1 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="exposure",
            inputs=[self],
            named_arguments={
                "exposure": exposure,
                "black": black,
            },
        )[0]

    def extractplanes(
        self, planes: Literal["y", "u", "v", "r", "g", "b", "a"] | None = None
    ) -> "FilterMultiOutput":
        """Extract planes as grayscale frames.

        Args:
            planes (str): set planes

                Allowed values:
                    * y: luma plane
                    * u: u plane
                    * v: v plane
                    * r: red plane
                    * g: green plane
                    * b: blue plane
                    * a: alpha plane

                Defaults to r.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="extractplanes",
            inputs=[self],
            named_arguments={
                "planes": planes,
            },
        )

    def extrastereo(self, m: float | None = None, c: bool | None = None) -> "Stream":
        """Increase difference between stereo audio channels.

        Args:
            m (float): set the difference coefficient (from -10 to 10)

                Defaults to 2.5.
            c (bool): enable clipping

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="extrastereo",
            inputs=[self],
            named_arguments={
                "m": m,
                "c": c,
            },
        )[0]

    def fade(
        self,
        type: Literal["in", "out"] | int | None = None,
        t: Literal["in", "out"] | int | None = None,
        start_frame: int | None = None,
        s: int | None = None,
        nb_frames: int | None = None,
        n: int | None = None,
        alpha: bool | None = None,
        start_time: str | None = None,
        st: str | None = None,
        duration: str | None = None,
        d: str | None = None,
        color: str | None = None,
        c: str | None = None,
    ) -> "Stream":
        """Fade in/out input video.

        Args:
            type (int | str): set the fade direction (from 0 to 1)

                Allowed values:
                    * in: fade-in
                    * out: fade-out

                Defaults to in.
            t (int | str): set the fade direction (from 0 to 1)

                Allowed values:
                    * in: fade-in
                    * out: fade-out

                Defaults to in.
            start_frame (int): Number of the first frame to which to apply the effect. (from 0 to INT_MAX)

                Defaults to 0.
            s (int): Number of the first frame to which to apply the effect. (from 0 to INT_MAX)

                Defaults to 0.
            nb_frames (int): Number of frames to which the effect should be applied. (from 1 to INT_MAX)

                Defaults to 25.
            n (int): Number of frames to which the effect should be applied. (from 1 to INT_MAX)

                Defaults to 25.
            alpha (bool): fade alpha if it is available on the input

                Defaults to false.
            start_time (str): Number of seconds of the beginning of the effect.

                Defaults to 0.
            st (str): Number of seconds of the beginning of the effect.

                Defaults to 0.
            duration (str): Duration of the effect in seconds.

                Defaults to 0.
            d (str): Duration of the effect in seconds.

                Defaults to 0.
            color (str): set color

                Defaults to black.
            c (str): set color

                Defaults to black.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fade",
            inputs=[self],
            named_arguments={
                "type": type,
                "t": t,
                "start_frame": start_frame,
                "s": s,
                "nb_frames": nb_frames,
                "n": n,
                "alpha": alpha,
                "start_time": start_time,
                "st": st,
                "duration": duration,
                "d": d,
                "color": color,
                "c": c,
            },
        )[0]

    def feedback(
        self,
        feedin_stream: "Stream",
        x: int | None = None,
        y: int | None = None,
        w: int | None = None,
        h: int | None = None,
    ) -> list["Stream"]:
        """Apply feedback video filter.

        Args:
            feedin_stream (Stream): Input video stream.
            x (int): set top left crop position (from 0 to INT_MAX)

                Defaults to 0.
            y (int): set top left crop position (from 0 to INT_MAX)

                Defaults to 0.
            w (int): set crop size (from 0 to INT_MAX)

                Defaults to 0.
            h (int): set crop size (from 0 to INT_MAX)

                Defaults to 0.

        Returns:
            list["Stream"]: A list of 2 Stream objects.
        """
        return self._apply_filter(
            filter_name="feedback",
            inputs=[self, feedin_stream],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            },
            num_output_streams=2,
        )

    def fftdnoiz(
        self,
        sigma: float | None = None,
        amount: float | None = None,
        block: int | None = None,
        overlap: float | None = None,
        method: Literal["wiener", "hard"] | int | None = None,
        prev: int | None = None,
        next: int | None = None,
        planes: int | None = None,
        window: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Denoise frames using 3D FFT.

        Args:
            sigma (float): set denoise strength (from 0 to 100)

                Defaults to 1.
            amount (float): set amount of denoising (from 0.01 to 1)

                Defaults to 1.
            block (int): set block size (from 8 to 256)

                Defaults to 32.
            overlap (float): set block overlap (from 0.2 to 0.8)

                Defaults to 0.5.
            method (int | str): set method of denoising (from 0 to 1)

                Allowed values:
                    * wiener: wiener method
                    * hard: hard thresholding

                Defaults to wiener.
            prev (int): set number of previous frames for temporal denoising (from 0 to 1)

                Defaults to 0.
            next (int): set number of next frames for temporal denoising (from 0 to 1)

                Defaults to 0.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 7.
            window (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fftdnoiz",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "amount": amount,
                "block": block,
                "overlap": overlap,
                "method": method,
                "prev": prev,
                "next": next,
                "planes": planes,
                "window": window,
            },
        )[0]

    def fftfilt(
        self,
        dc_Y: int | None = None,
        dc_U: int | None = None,
        dc_V: int | None = None,
        weight_Y: str | None = None,
        weight_U: str | None = None,
        weight_V: str | None = None,
        eval: Literal["init", "frame"] | int | None = None,
    ) -> "Stream":
        """Apply arbitrary expressions to pixels in frequency domain.

        Args:
            dc_Y (int): adjust gain in Y plane (from 0 to 1000)

                Defaults to 0.
            dc_U (int): adjust gain in U plane (from 0 to 1000)

                Defaults to 0.
            dc_V (int): adjust gain in V plane (from 0 to 1000)

                Defaults to 0.
            weight_Y (str): set luminance expression in Y plane

                Defaults to 1.
            weight_U (str): set chrominance expression in U plane

            weight_V (str): set chrominance expression in V plane

            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions per-frame

                Defaults to init.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fftfilt",
            inputs=[self],
            named_arguments={
                "dc_Y": dc_Y,
                "dc_U": dc_U,
                "dc_V": dc_V,
                "weight_Y": weight_Y,
                "weight_U": weight_U,
                "weight_V": weight_V,
                "eval": eval,
            },
        )[0]

    def field(self, type: Literal["top", "bottom"] | int | None = None) -> "Stream":
        """Extract a field from the input video.

        Args:
            type (int | str): set field type (top or bottom) (from 0 to 1)

                Allowed values:
                    * top: select top field
                    * bottom: select bottom field

                Defaults to top.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="field",
            inputs=[self],
            named_arguments={
                "type": type,
            },
        )[0]

    def fieldhint(
        self,
        hint: str | None = None,
        mode: Literal["absolute", "relative", "pattern"] | int | None = None,
    ) -> "Stream":
        """Field matching using hints.

        Args:
            hint (str): set hint file

            mode (int | str): set hint mode (from 0 to 2)

                Allowed values:
                    * absolute
                    * relative
                    * pattern

                Defaults to absolute.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fieldhint",
            inputs=[self],
            named_arguments={
                "hint": hint,
                "mode": mode,
            },
        )[0]

    def fieldmatch(
        self,
        *streams: "Stream",
        order: Literal["auto", "bff", "tff"] | int | None = None,
        mode: Literal["pc", "pc_n", "pc_u", "pc_n_ub", "pcn", "pcn_ub"]
        | int
        | None = None,
        ppsrc: bool | None = None,
        field: Literal["auto", "bottom", "top"] | int | None = None,
        mchroma: bool | None = None,
        y0: int | None = None,
        y1: int | None = None,
        scthresh: float | None = None,
        combmatch: Literal["none", "sc", "full"] | int | None = None,
        combdbg: Literal["none", "pcn", "pcnub"] | int | None = None,
        cthresh: int | None = None,
        chroma: bool | None = None,
        blockx: int | None = None,
        blocky: int | None = None,
        combpel: int | None = None,
    ) -> "Stream":
        """Field matching for inverse telecine.

        Args:
            *streams (Stream): One or more input streams.
            order (int | str): specify the assumed field order (from -1 to 1)

                Allowed values:
                    * auto: auto detect parity
                    * bff: assume bottom field first
                    * tff: assume top field first

                Defaults to auto.
            mode (int | str): set the matching mode or strategy to use (from 0 to 5)

                Allowed values:
                    * pc: 2-way match (p/c)
                    * pc_n: 2-way match + 3rd match on combed (p/c + u)
                    * pc_u: 2-way match + 3rd match (same order) on combed (p/c + u)
                    * pc_n_ub: 2-way match + 3rd match on combed + 4th/5th matches if still combed (p/c + u + u/b)
                    * pcn: 3-way match (p/c/n)
                    * pcn_ub: 3-way match + 4th/5th matches on combed (p/c/n + u/b)

                Defaults to pc_n.
            ppsrc (bool): mark main input as a pre-processed input and activate clean source input stream

                Defaults to false.
            field (int | str): set the field to match from (from -1 to 1)

                Allowed values:
                    * auto: automatic (same value as 'order')
                    * bottom: bottom field
                    * top: top field

                Defaults to auto.
            mchroma (bool): set whether or not chroma is included during the match comparisons

                Defaults to true.
            y0 (int): define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX)

                Defaults to 0.
            y1 (int): define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX)

                Defaults to 0.
            scthresh (float): set scene change detection threshold (from 0 to 100)

                Defaults to 12.
            combmatch (int | str): set combmatching mode (from 0 to 2)

                Allowed values:
                    * none: disable combmatching
                    * sc: enable combmatching only on scene change
                    * full: enable combmatching all the time

                Defaults to sc.
            combdbg (int | str): enable comb debug (from 0 to 2)

                Allowed values:
                    * none: no forced calculation
                    * pcn: calculate p/c/n
                    * pcnub: calculate p/c/n/u/b

                Defaults to none.
            cthresh (int): set the area combing threshold used for combed frame detection (from -1 to 255)

                Defaults to 9.
            chroma (bool): set whether or not chroma is considered in the combed frame decision

                Defaults to false.
            blockx (int): set the x-axis size of the window used during combed frame detection (from 4 to 512)

                Defaults to 16.
            blocky (int): set the y-axis size of the window used during combed frame detection (from 4 to 512)

                Defaults to 16.
            combpel (int): set the number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed (from 0 to INT_MAX)

                Defaults to 80.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fieldmatch",
            inputs=[self, *streams],
            named_arguments={
                "order": order,
                "mode": mode,
                "ppsrc": ppsrc,
                "field": field,
                "mchroma": mchroma,
                "y0": y0,
                "y1": y1,
                "scthresh": scthresh,
                "combmatch": combmatch,
                "combdbg": combdbg,
                "cthresh": cthresh,
                "chroma": chroma,
                "blockx": blockx,
                "blocky": blocky,
                "combpel": combpel,
            },
        )[0]

    def fieldorder(self, order: Literal["bff", "tff"] | int | None = None) -> "Stream":
        """Set the field order.

        Args:
            order (int | str): output field order (from 0 to 1)

                Allowed values:
                    * bff: bottom field first
                    * tff: top field first

                Defaults to tff.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fieldorder",
            inputs=[self],
            named_arguments={
                "order": order,
            },
        )[0]

    def fillborders(
        self,
        left: int | None = None,
        right: int | None = None,
        top: int | None = None,
        bottom: int | None = None,
        mode: Literal["smear", "mirror", "fixed", "reflect", "wrap", "fade", "margins"]
        | int
        | None = None,
        color: str | None = None,
    ) -> "Stream":
        """Fill borders of the input video.

        Args:
            left (int): set the left fill border (from 0 to INT_MAX)

                Defaults to 0.
            right (int): set the right fill border (from 0 to INT_MAX)

                Defaults to 0.
            top (int): set the top fill border (from 0 to INT_MAX)

                Defaults to 0.
            bottom (int): set the bottom fill border (from 0 to INT_MAX)

                Defaults to 0.
            mode (int | str): set the fill borders mode (from 0 to 6)

                Allowed values:
                    * smear
                    * mirror
                    * fixed
                    * reflect
                    * wrap
                    * fade
                    * margins

                Defaults to smear.
            color (str): set the color for the fixed/fade mode

                Defaults to black.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fillborders",
            inputs=[self],
            named_arguments={
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
                "mode": mode,
                "color": color,
            },
        )[0]

    def find_rect(
        self,
        object: str | None = None,
        threshold: float | None = None,
        mipmaps: int | None = None,
        xmin: int | None = None,
        ymin: int | None = None,
        xmax: int | None = None,
        ymax: int | None = None,
        discard: bool | None = None,
    ) -> "Stream":
        """Find a user specified object.

        Args:
            object (str): object bitmap filename

            threshold (float): set threshold (from 0 to 1)

                Defaults to 0.5.
            mipmaps (int): set mipmaps (from 1 to 5)

                Defaults to 3.
            xmin (int): (from 0 to INT_MAX)

                Defaults to 0.
            ymin (int): (from 0 to INT_MAX)

                Defaults to 0.
            xmax (int): (from 0 to INT_MAX)

                Defaults to 0.
            ymax (int): (from 0 to INT_MAX)

                Defaults to 0.
            discard (bool): No description available.

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="find_rect",
            inputs=[self],
            named_arguments={
                "object": object,
                "threshold": threshold,
                "mipmaps": mipmaps,
                "xmin": xmin,
                "ymin": ymin,
                "xmax": xmax,
                "ymax": ymax,
                "discard": discard,
            },
        )[0]

    def firequalizer(
        self,
        gain: str | None = None,
        gain_entry: str | None = None,
        delay: float | None = None,
        accuracy: float | None = None,
        wfunc: Literal[
            "rectangular",
            "hann",
            "hamming",
            "blackman",
            "nuttall3",
            "mnuttall3",
            "nuttall",
            "bnuttall",
            "bharris",
            "tukey",
        ]
        | int
        | None = None,
        fixed: bool | None = None,
        multi: bool | None = None,
        zero_phase: bool | None = None,
        scale: Literal["linlin", "linlog", "loglin", "loglog"] | int | None = None,
        dumpfile: str | None = None,
        dumpscale: Literal["linlin", "linlog", "loglin", "loglog"] | int | None = None,
        fft2: bool | None = None,
        min_phase: bool | None = None,
    ) -> "Stream":
        """Finite Impulse Response Equalizer.

        Args:
            gain (str): set gain curve

                Defaults to gain_interpolate(f).
            gain_entry (str): set gain entry

            delay (float): set delay (from 0 to 1e+10)

                Defaults to 0.01.
            accuracy (float): set accuracy (from 0 to 1e+10)

                Defaults to 5.
            wfunc (int | str): set window function (from 0 to 9)

                Allowed values:
                    * rectangular: rectangular window
                    * hann: hann window
                    * hamming: hamming window
                    * blackman: blackman window
                    * nuttall3: 3-term nuttall window
                    * mnuttall3: minimum 3-term nuttall window
                    * nuttall: nuttall window
                    * bnuttall: blackman-nuttall window
                    * bharris: blackman-harris window
                    * tukey: tukey window

                Defaults to hann.
            fixed (bool): set fixed frame samples

                Defaults to false.
            multi (bool): set multi channels mode

                Defaults to false.
            zero_phase (bool): set zero phase mode

                Defaults to false.
            scale (int | str): set gain scale (from 0 to 3)

                Allowed values:
                    * linlin: linear-freq linear-gain
                    * linlog: linear-freq logarithmic-gain
                    * loglin: logarithmic-freq linear-gain
                    * loglog: logarithmic-freq logarithmic-gain

                Defaults to linlog.
            dumpfile (str): set dump file

            dumpscale (int | str): set dump scale (from 0 to 3)

                Allowed values:
                    * linlin: linear-freq linear-gain
                    * linlog: linear-freq logarithmic-gain
                    * loglin: logarithmic-freq linear-gain
                    * loglog: logarithmic-freq logarithmic-gain

                Defaults to linlog.
            fft2 (bool): set 2-channels fft

                Defaults to false.
            min_phase (bool): set minimum phase mode

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="firequalizer",
            inputs=[self],
            named_arguments={
                "gain": gain,
                "gain_entry": gain_entry,
                "delay": delay,
                "accuracy": accuracy,
                "wfunc": wfunc,
                "fixed": fixed,
                "multi": multi,
                "zero_phase": zero_phase,
                "scale": scale,
                "dumpfile": dumpfile,
                "dumpscale": dumpscale,
                "fft2": fft2,
                "min_phase": min_phase,
            },
        )[0]

    def flanger(
        self,
        delay: float | None = None,
        depth: float | None = None,
        regen: float | None = None,
        width: float | None = None,
        speed: float | None = None,
        shape: Literal["triangular", "t", "sinusoidal", "s"] | int | None = None,
        phase: float | None = None,
        interp: Literal["linear", "quadratic"] | int | None = None,
    ) -> "Stream":
        """Apply a flanging effect to the audio.

        Args:
            delay (float): base delay in milliseconds (from 0 to 30)

                Defaults to 0.
            depth (float): added swept delay in milliseconds (from 0 to 10)

                Defaults to 2.
            regen (float): percentage regeneration (delayed signal feedback) (from -95 to 95)

                Defaults to 0.
            width (float): percentage of delayed signal mixed with original (from 0 to 100)

                Defaults to 71.
            speed (float): sweeps per second (Hz) (from 0.1 to 10)

                Defaults to 0.5.
            shape (int | str): swept wave shape (from 0 to 1)

                Allowed values:
                    * triangular
                    * t
                    * sinusoidal
                    * s

                Defaults to sinusoidal.
            phase (float): swept wave percentage phase-shift for multi-channel (from 0 to 100)

                Defaults to 25.
            interp (int | str): delay-line interpolation (from 0 to 1)

                Allowed values:
                    * linear
                    * quadratic

                Defaults to linear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="flanger",
            inputs=[self],
            named_arguments={
                "delay": delay,
                "depth": depth,
                "regen": regen,
                "width": width,
                "speed": speed,
                "shape": shape,
                "phase": phase,
                "interp": interp,
            },
        )[0]

    def floodfill(
        self,
        x: int | None = None,
        y: int | None = None,
        s0: int | None = None,
        s1: int | None = None,
        s2: int | None = None,
        s3: int | None = None,
        d0: int | None = None,
        d1: int | None = None,
        d2: int | None = None,
        d3: int | None = None,
    ) -> "Stream":
        """Fill area with same color with another color.

        Args:
            x (int): set pixel x coordinate (from 0 to 65535)

                Defaults to 0.
            y (int): set pixel y coordinate (from 0 to 65535)

                Defaults to 0.
            s0 (int): set source #0 component value (from -1 to 65535)

                Defaults to 0.
            s1 (int): set source #1 component value (from -1 to 65535)

                Defaults to 0.
            s2 (int): set source #2 component value (from -1 to 65535)

                Defaults to 0.
            s3 (int): set source #3 component value (from -1 to 65535)

                Defaults to 0.
            d0 (int): set destination #0 component value (from 0 to 65535)

                Defaults to 0.
            d1 (int): set destination #1 component value (from 0 to 65535)

                Defaults to 0.
            d2 (int): set destination #2 component value (from 0 to 65535)

                Defaults to 0.
            d3 (int): set destination #3 component value (from 0 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="floodfill",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "s0": s0,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "d0": d0,
                "d1": d1,
                "d2": d2,
                "d3": d3,
            },
        )[0]

    def format(
        self,
        pix_fmts: str | None = None,
        color_spaces: str | None = None,
        color_ranges: str | None = None,
    ) -> "Stream":
        """Convert the input video to one of the specified pixel formats.

        Args:
            pix_fmts (str): A '|'-separated list of pixel formats

            color_spaces (str): A '|'-separated list of color spaces

            color_ranges (str): A '|'-separated list of color ranges


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="format",
            inputs=[self],
            named_arguments={
                "pix_fmts": pix_fmts,
                "color_spaces": color_spaces,
                "color_ranges": color_ranges,
            },
        )[0]

    def fps(
        self,
        fps: str | None = None,
        start_time: float | None = None,
        round: Literal["zero", "inf", "down", "up", "near"] | int | None = None,
        eof_action: Literal["round", "pass"] | int | None = None,
    ) -> "Stream":
        """Force constant framerate.

        Args:
            fps (str): A string describing desired output framerate

                Defaults to 25.
            start_time (float): Assume the first PTS should be this value. (from -DBL_MAX to DBL_MAX)

                Defaults to DBL_MAX.
            round (int | str): set rounding method for timestamps (from 0 to 5)

                Allowed values:
                    * zero: round towards 0
                    * inf: round away from 0
                    * down: round towards -infty
                    * up: round towards +infty
                    * near: round to nearest

                Defaults to near.
            eof_action (int | str): action performed for last frame (from 0 to 1)

                Allowed values:
                    * round: round similar to other frames
                    * pass: pass through last frame

                Defaults to round.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fps",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "start_time": start_time,
                "round": round,
                "eof_action": eof_action,
            },
        )[0]

    def framepack(
        self,
        right_stream: "Stream",
        format: Literal["sbs", "tab", "frameseq", "lines", "columns"]
        | int
        | None = None,
    ) -> "Stream":
        """Generate a frame packed stereoscopic video.

        Args:
            right_stream (Stream): Input video stream.
            format (int | str): Frame pack output format (from 0 to INT_MAX)

                Allowed values:
                    * sbs: Views are packed next to each other
                    * tab: Views are packed on top of each other
                    * frameseq: Views are one after the other
                    * lines: Views are interleaved by lines
                    * columns: Views are interleaved by columns

                Defaults to sbs.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="framepack",
            inputs=[self, right_stream],
            named_arguments={
                "format": format,
            },
        )[0]

    def framerate(
        self,
        fps: str | None = None,
        interp_start: int | None = None,
        interp_end: int | None = None,
        scene: float | None = None,
        flags: Literal["scene_change_detect", "scd"] | None = None,
    ) -> "Stream":
        """Upsamples or downsamples progressive source between specified frame rates.

        Args:
            fps (str): required output frames per second rate

                Defaults to 50.
            interp_start (int): point to start linear interpolation (from 0 to 255)

                Defaults to 15.
            interp_end (int): point to end linear interpolation (from 0 to 255)

                Defaults to 240.
            scene (float): scene change level (from 0 to 100)

                Defaults to 8.2.
            flags (str): set flags

                Allowed values:
                    * scene_change_detect: scene change detection
                    * scd: scene change detection

                Defaults to scene_change_detect+scd.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="framerate",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "interp_start": interp_start,
                "interp_end": interp_end,
                "scene": scene,
                "flags": flags,
            },
        )[0]

    def framestep(self, step: int | None = None) -> "Stream":
        """Select one frame every N frames.

        Args:
            step (int): set frame step (from 1 to INT_MAX)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="framestep",
            inputs=[self],
            named_arguments={
                "step": step,
            },
        )[0]

    def freezedetect(
        self,
        n: float | None = None,
        noise: float | None = None,
        d: str | None = None,
        duration: str | None = None,
    ) -> "Stream":
        """Detects frozen video input.

        Args:
            n (float): set noise tolerance (from 0 to 1)

                Defaults to 0.001.
            noise (float): set noise tolerance (from 0 to 1)

                Defaults to 0.001.
            d (str): set minimum duration in seconds

                Defaults to 2.
            duration (str): set minimum duration in seconds

                Defaults to 2.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="freezedetect",
            inputs=[self],
            named_arguments={
                "n": n,
                "noise": noise,
                "d": d,
                "duration": duration,
            },
        )[0]

    def freezeframes(
        self,
        replace_stream: "Stream",
        first: str | None = None,
        last: str | None = None,
        replace: str | None = None,
    ) -> "Stream":
        """Freeze video frames.

        Args:
            replace_stream (Stream): Input video stream.
            first (str): set first frame to freeze (from 0 to I64_MAX)

                Defaults to 0.
            last (str): set last frame to freeze (from 0 to I64_MAX)

                Defaults to 0.
            replace (str): set frame to replace (from 0 to I64_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="freezeframes",
            inputs=[self, replace_stream],
            named_arguments={
                "first": first,
                "last": last,
                "replace": replace,
            },
        )[0]

    def frei0r(
        self, filter_name: str | None = None, filter_params: str | None = None
    ) -> "Stream":
        """Apply a frei0r effect.

        Args:
            filter_name (str): No description available.

            filter_params (str): No description available.


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="frei0r",
            inputs=[self],
            named_arguments={
                "filter_name": filter_name,
                "filter_params": filter_params,
            },
        )[0]

    def fspp(
        self,
        quality: int | None = None,
        qp: int | None = None,
        strength: int | None = None,
        use_bframe_qp: bool | None = None,
    ) -> "Stream":
        """Apply Fast Simple Post-processing filter.

        Args:
            quality (int): set quality (from 4 to 5)

                Defaults to 4.
            qp (int): force a constant quantizer parameter (from 0 to 64)

                Defaults to 0.
            strength (int): set filter strength (from -15 to 32)

                Defaults to 0.
            use_bframe_qp (bool): use B-frames' QP

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fspp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "strength": strength,
                "use_bframe_qp": use_bframe_qp,
            },
        )[0]

    def fsync(self, file: str | None = None, f: str | None = None) -> "Stream":
        """Synchronize video frames from external source.

        Args:
            file (str): set the file name to use for frame sync

            f (str): set the file name to use for frame sync


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="fsync",
            inputs=[self],
            named_arguments={
                "file": file,
                "f": f,
            },
        )[0]

    def gblur(
        self,
        sigma: float | None = None,
        steps: int | None = None,
        planes: int | None = None,
        sigmaV: float | None = None,
    ) -> "Stream":
        """Apply Gaussian Blur filter.

        Args:
            sigma (float): set sigma (from 0 to 1024)

                Defaults to 0.5.
            steps (int): set number of steps (from 1 to 6)

                Defaults to 1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            sigmaV (float): set vertical sigma (from -1 to 1024)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="gblur",
            inputs=[self],
            named_arguments={
                "sigma": sigma,
                "steps": steps,
                "planes": planes,
                "sigmaV": sigmaV,
            },
        )[0]

    def geq(
        self,
        lum_expr: str | None = None,
        lum: str | None = None,
        cb_expr: str | None = None,
        cb: str | None = None,
        cr_expr: str | None = None,
        cr: str | None = None,
        alpha_expr: str | None = None,
        a: str | None = None,
        red_expr: str | None = None,
        r: str | None = None,
        green_expr: str | None = None,
        g: str | None = None,
        blue_expr: str | None = None,
        b: str | None = None,
        interpolation: Literal["nearest", "n", "bilinear", "b"] | int | None = None,
        i: Literal["nearest", "n", "bilinear", "b"] | int | None = None,
    ) -> "Stream":
        """Apply generic equation to each pixel.

        Args:
            lum_expr (str): set luminance expression

            lum (str): set luminance expression

            cb_expr (str): set chroma blue expression

            cb (str): set chroma blue expression

            cr_expr (str): set chroma red expression

            cr (str): set chroma red expression

            alpha_expr (str): set alpha expression

            a (str): set alpha expression

            red_expr (str): set red expression

            r (str): set red expression

            green_expr (str): set green expression

            g (str): set green expression

            blue_expr (str): set blue expression

            b (str): set blue expression

            interpolation (int | str): set interpolation method (from 0 to 1)

                Allowed values:
                    * nearest: nearest interpolation
                    * n: nearest interpolation
                    * bilinear: bilinear interpolation
                    * b: bilinear interpolation

                Defaults to bilinear.
            i (int | str): set interpolation method (from 0 to 1)

                Allowed values:
                    * nearest: nearest interpolation
                    * n: nearest interpolation
                    * bilinear: bilinear interpolation
                    * b: bilinear interpolation

                Defaults to bilinear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="geq",
            inputs=[self],
            named_arguments={
                "lum_expr": lum_expr,
                "lum": lum,
                "cb_expr": cb_expr,
                "cb": cb,
                "cr_expr": cr_expr,
                "cr": cr,
                "alpha_expr": alpha_expr,
                "a": a,
                "red_expr": red_expr,
                "r": r,
                "green_expr": green_expr,
                "g": g,
                "blue_expr": blue_expr,
                "b": b,
                "interpolation": interpolation,
                "i": i,
            },
        )[0]

    def gradfun(
        self, strength: float | None = None, radius: int | None = None
    ) -> "Stream":
        """Debands video quickly using gradients.

        Args:
            strength (float): The maximum amount by which the filter will change any one pixel. (from 0.51 to 64)

                Defaults to 1.2.
            radius (int): The neighborhood to fit the gradient to. (from 4 to 32)

                Defaults to 16.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="gradfun",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "radius": radius,
            },
        )[0]

    def graphmonitor(
        self,
        size: str | None = None,
        s: str | None = None,
        opacity: float | None = None,
        o: float | None = None,
        mode: Literal["full", "compact", "nozero", "noeof", "nodisabled"] | None = None,
        m: Literal["full", "compact", "nozero", "noeof", "nodisabled"] | None = None,
        flags: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ]
        | None = None,
        f: Literal[
            "none",
            "all",
            "queue",
            "frame_count_in",
            "frame_count_out",
            "frame_count_delta",
            "pts",
            "pts_delta",
            "time",
            "time_delta",
            "timebase",
            "format",
            "size",
            "rate",
            "eof",
            "sample_count_in",
            "sample_count_out",
            "sample_count_delta",
            "disabled",
        ]
        | None = None,
        rate: str | None = None,
        r: str | None = None,
    ) -> "Stream":
        """Show various filtergraph stats.

        Args:
            size (str): set monitor size

                Defaults to hd720.
            s (str): set monitor size

                Defaults to hd720.
            opacity (float): set video opacity (from 0 to 1)

                Defaults to 0.9.
            o (float): set video opacity (from 0 to 1)

                Defaults to 0.9.
            mode (str): set mode

                Allowed values:
                    * full
                    * compact
                    * nozero
                    * noeof
                    * nodisabled

                Defaults to 0.
            m (str): set mode

                Allowed values:
                    * full
                    * compact
                    * nozero
                    * noeof
                    * nodisabled

                Defaults to 0.
            flags (str): set flags

                Allowed values:
                    * none
                    * all
                    * queue
                    * frame_count_in
                    * frame_count_out
                    * frame_count_delta
                    * pts
                    * pts_delta
                    * time
                    * time_delta
                    * timebase
                    * format
                    * size
                    * rate
                    * eof
                    * sample_count_in
                    * sample_count_out
                    * sample_count_delta
                    * disabled

                Defaults to all+queue.
            f (str): set flags

                Allowed values:
                    * none
                    * all
                    * queue
                    * frame_count_in
                    * frame_count_out
                    * frame_count_delta
                    * pts
                    * pts_delta
                    * time
                    * time_delta
                    * timebase
                    * format
                    * size
                    * rate
                    * eof
                    * sample_count_in
                    * sample_count_out
                    * sample_count_delta
                    * disabled

                Defaults to all+queue.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="graphmonitor",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "opacity": opacity,
                "o": o,
                "mode": mode,
                "m": m,
                "flags": flags,
                "f": f,
                "rate": rate,
                "r": r,
            },
        )[0]

    def grayworld(
        self,
    ) -> "Stream":
        """Adjust white balance using LAB gray world algorithm

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="grayworld", inputs=[self], named_arguments={}
        )[0]

    def greyedge(
        self,
        difford: int | None = None,
        minknorm: int | None = None,
        sigma: float | None = None,
    ) -> "Stream":
        """Estimates scene illumination by grey edge assumption.

        Args:
            difford (int): set differentiation order (from 0 to 2)

                Defaults to 1.
            minknorm (int): set Minkowski norm (from 0 to 20)

                Defaults to 1.
            sigma (float): set sigma (from 0 to 1024)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="greyedge",
            inputs=[self],
            named_arguments={
                "difford": difford,
                "minknorm": minknorm,
                "sigma": sigma,
            },
        )[0]

    def guided(
        self,
        *streams: "Stream",
        radius: int | None = None,
        eps: float | None = None,
        mode: Literal["basic", "fast"] | int | None = None,
        sub: int | None = None,
        guidance: Literal["off", "on"] | int | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply Guided filter.

        Args:
            *streams (Stream): One or more input streams.
            radius (int): set the box radius (from 1 to 20)

                Defaults to 3.
            eps (float): set the regularization parameter (with square) (from 0 to 1)

                Defaults to 0.01.
            mode (int | str): set filtering mode (0: basic mode; 1: fast mode) (from 0 to 1)

                Allowed values:
                    * basic: basic guided filter
                    * fast: fast guided filter

                Defaults to basic.
            sub (int): subsampling ratio for fast mode (from 2 to 64)

                Defaults to 4.
            guidance (int | str): set guidance mode (0: off mode; 1: on mode) (from 0 to 1)

                Allowed values:
                    * off: only one input is enabled
                    * on: two inputs are required

                Defaults to off.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="guided",
            inputs=[self, *streams],
            named_arguments={
                "radius": radius,
                "eps": eps,
                "mode": mode,
                "sub": sub,
                "guidance": guidance,
                "planes": planes,
            },
        )[0]

    def haas(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        side_gain: float | None = None,
        middle_source: Literal["left", "right", "mid", "side"] | int | None = None,
        middle_phase: bool | None = None,
        left_delay: float | None = None,
        left_balance: float | None = None,
        left_gain: float | None = None,
        left_phase: bool | None = None,
        right_delay: float | None = None,
        right_balance: float | None = None,
        right_gain: float | None = None,
        right_phase: bool | None = None,
    ) -> "Stream":
        """Apply Haas Stereo Enhancer.

        Args:
            level_in (float): set level in (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set level out (from 0.015625 to 64)

                Defaults to 1.
            side_gain (float): set side gain (from 0.015625 to 64)

                Defaults to 1.
            middle_source (int | str): set middle source (from 0 to 3)

                Allowed values:
                    * left
                    * right
                    * mid: L+R
                    * side: L-R

                Defaults to mid.
            middle_phase (bool): set middle phase

                Defaults to false.
            left_delay (float): set left delay (from 0 to 40)

                Defaults to 2.05.
            left_balance (float): set left balance (from -1 to 1)

                Defaults to -1.
            left_gain (float): set left gain (from 0.015625 to 64)

                Defaults to 1.
            left_phase (bool): set left phase

                Defaults to false.
            right_delay (float): set right delay (from 0 to 40)

                Defaults to 2.12.
            right_balance (float): set right balance (from -1 to 1)

                Defaults to 1.
            right_gain (float): set right gain (from 0.015625 to 64)

                Defaults to 1.
            right_phase (bool): set right phase

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="haas",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "side_gain": side_gain,
                "middle_source": middle_source,
                "middle_phase": middle_phase,
                "left_delay": left_delay,
                "left_balance": left_balance,
                "left_gain": left_gain,
                "left_phase": left_phase,
                "right_delay": right_delay,
                "right_balance": right_balance,
                "right_gain": right_gain,
                "right_phase": right_phase,
            },
        )[0]

    def haldclut(
        self,
        clut_stream: "Stream",
        clut: Literal["first", "all"] | int | None = None,
        interp: Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | int
        | None = None,
    ) -> "Stream":
        """Adjust colors using a Hald CLUT.

        Args:
            clut_stream (Stream): Input video stream.
            clut (int | str): when to process CLUT (from 0 to 1)

                Allowed values:
                    * first: process only first CLUT, ignore rest
                    * all: process all CLUTs

                Defaults to all.
            interp (int | str): select interpolation mode (from 0 to 4)

                Allowed values:
                    * nearest: use values from the nearest defined points
                    * trilinear: interpolate values using the 8 points defining a cube
                    * tetrahedral: interpolate values using a tetrahedron
                    * pyramid: interpolate values using a pyramid
                    * prism: interpolate values using a prism

                Defaults to tetrahedral.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="haldclut",
            inputs=[self, clut_stream],
            named_arguments={
                "clut": clut,
                "interp": interp,
            },
        )[0]

    def hdcd(
        self,
        disable_autoconvert: bool | None = None,
        process_stereo: bool | None = None,
        cdt_ms: int | None = None,
        force_pe: bool | None = None,
        analyze_mode: Literal["off", "lle", "pe", "cdt", "tgm"] | int | None = None,
        bits_per_sample: Literal["16", "20", "24"] | int | None = None,
    ) -> "Stream":
        """Apply High Definition Compatible Digital (HDCD) decoding.

        Args:
            disable_autoconvert (bool): Disable any format conversion or resampling in the filter graph.

                Defaults to true.
            process_stereo (bool): Process stereo channels together. Only apply target_gain when both channels match.

                Defaults to true.
            cdt_ms (int): Code detect timer period in ms. (from 100 to 60000)

                Defaults to 2000.
            force_pe (bool): Always extend peaks above -3dBFS even when PE is not signaled.

                Defaults to false.
            analyze_mode (int | str): Replace audio with solid tone and signal some processing aspect in the amplitude. (from 0 to 4)

                Allowed values:
                    * off: disabled
                    * lle: gain adjustment level at each sample
                    * pe: samples where peak extend occurs
                    * cdt: samples where the code detect timer is active
                    * tgm: samples where the target gain does not match between channels

                Defaults to off.
            bits_per_sample (int | str): Valid bits per sample (location of the true LSB). (from 16 to 24)

                Allowed values:
                    * 16: 16-bit (in s32 or s16)
                    * 20: 20-bit (in s32)
                    * 24: 24-bit (in s32)

                Defaults to 16.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hdcd",
            inputs=[self],
            named_arguments={
                "disable_autoconvert": disable_autoconvert,
                "process_stereo": process_stereo,
                "cdt_ms": cdt_ms,
                "force_pe": force_pe,
                "analyze_mode": analyze_mode,
                "bits_per_sample": bits_per_sample,
            },
        )[0]

    def headphone(
        self,
        *streams: "Stream",
        map: str | None = None,
        gain: float | None = None,
        lfe: float | None = None,
        type: Literal["time", "freq"] | int | None = None,
        size: int | None = None,
        hrir: Literal["stereo", "multich"] | int | None = None,
    ) -> "Stream":
        """Apply headphone binaural spatialization with HRTFs in additional streams.

        Args:
            *streams (Stream): One or more input streams.
            map (str): set channels convolution mappings

            gain (float): set gain in dB (from -20 to 40)

                Defaults to 0.
            lfe (float): set lfe gain in dB (from -20 to 40)

                Defaults to 0.
            type (int | str): set processing (from 0 to 1)

                Allowed values:
                    * time: time domain
                    * freq: frequency domain

                Defaults to freq.
            size (int): set frame size (from 1024 to 96000)

                Defaults to 1024.
            hrir (int | str): set hrir format (from 0 to 1)

                Allowed values:
                    * stereo: hrir files have exactly 2 channels
                    * multich: single multichannel hrir file

                Defaults to stereo.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="headphone",
            inputs=[self, *streams],
            named_arguments={
                "map": map,
                "gain": gain,
                "lfe": lfe,
                "type": type,
                "size": size,
                "hrir": hrir,
            },
        )[0]

    def hflip(
        self,
    ) -> "Stream":
        """Horizontally flip the input video.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hflip", inputs=[self], named_arguments={}
        )[0]

    def highpass(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a high-pass filter with 3dB point frequency.

        Args:
            frequency (float): set frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.707.
            w (float): set width (from 0 to 99999)

                Defaults to 0.707.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="highpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def highshelf(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a high shelf filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="highshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def histeq(
        self,
        strength: float | None = None,
        intensity: float | None = None,
        antibanding: Literal["none", "weak", "strong"] | int | None = None,
    ) -> "Stream":
        """Apply global color histogram equalization.

        Args:
            strength (float): set the strength (from 0 to 1)

                Defaults to 0.2.
            intensity (float): set the intensity (from 0 to 1)

                Defaults to 0.21.
            antibanding (int | str): set the antibanding level (from 0 to 2)

                Allowed values:
                    * none: apply no antibanding
                    * weak: apply weak antibanding
                    * strong: apply strong antibanding

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="histeq",
            inputs=[self],
            named_arguments={
                "strength": strength,
                "intensity": intensity,
                "antibanding": antibanding,
            },
        )[0]

    def histogram(
        self,
        level_height: int | None = None,
        scale_height: int | None = None,
        display_mode: Literal["overlay", "parade", "stack"] | int | None = None,
        d: Literal["overlay", "parade", "stack"] | int | None = None,
        levels_mode: Literal["linear", "logarithmic"] | int | None = None,
        m: Literal["linear", "logarithmic"] | int | None = None,
        components: int | None = None,
        c: int | None = None,
        fgopacity: float | None = None,
        f: float | None = None,
        bgopacity: float | None = None,
        b: float | None = None,
        colors_mode: Literal[
            "whiteonblack",
            "blackonwhite",
            "whiteongray",
            "blackongray",
            "coloronblack",
            "coloronwhite",
            "colorongray",
            "blackoncolor",
            "whiteoncolor",
            "grayoncolor",
        ]
        | int
        | None = None,
        l: Literal[
            "whiteonblack",
            "blackonwhite",
            "whiteongray",
            "blackongray",
            "coloronblack",
            "coloronwhite",
            "colorongray",
            "blackoncolor",
            "whiteoncolor",
            "grayoncolor",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Compute and draw a histogram.

        Args:
            level_height (int): set level height (from 50 to 2048)

                Defaults to 200.
            scale_height (int): set scale height (from 0 to 40)

                Defaults to 12.
            display_mode (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * parade
                    * stack

                Defaults to stack.
            d (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * parade
                    * stack

                Defaults to stack.
            levels_mode (int | str): set levels mode (from 0 to 1)

                Allowed values:
                    * linear
                    * logarithmic

                Defaults to linear.
            m (int | str): set levels mode (from 0 to 1)

                Allowed values:
                    * linear
                    * logarithmic

                Defaults to linear.
            components (int): set color components to display (from 1 to 15)

                Defaults to 7.
            c (int): set color components to display (from 1 to 15)

                Defaults to 7.
            fgopacity (float): set foreground opacity (from 0 to 1)

                Defaults to 0.7.
            f (float): set foreground opacity (from 0 to 1)

                Defaults to 0.7.
            bgopacity (float): set background opacity (from 0 to 1)

                Defaults to 0.5.
            b (float): set background opacity (from 0 to 1)

                Defaults to 0.5.
            colors_mode (int | str): set colors mode (from 0 to 9)

                Allowed values:
                    * whiteonblack
                    * blackonwhite
                    * whiteongray
                    * blackongray
                    * coloronblack
                    * coloronwhite
                    * colorongray
                    * blackoncolor
                    * whiteoncolor
                    * grayoncolor

                Defaults to whiteonblack.
            l (int | str): set colors mode (from 0 to 9)

                Allowed values:
                    * whiteonblack
                    * blackonwhite
                    * whiteongray
                    * blackongray
                    * coloronblack
                    * coloronwhite
                    * colorongray
                    * blackoncolor
                    * whiteoncolor
                    * grayoncolor

                Defaults to whiteonblack.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="histogram",
            inputs=[self],
            named_arguments={
                "level_height": level_height,
                "scale_height": scale_height,
                "display_mode": display_mode,
                "d": d,
                "levels_mode": levels_mode,
                "m": m,
                "components": components,
                "c": c,
                "fgopacity": fgopacity,
                "f": f,
                "bgopacity": bgopacity,
                "b": b,
                "colors_mode": colors_mode,
                "l": l,
            },
        )[0]

    def hqdn3d(
        self,
        luma_spatial: float | None = None,
        chroma_spatial: float | None = None,
        luma_tmp: float | None = None,
        chroma_tmp: float | None = None,
    ) -> "Stream":
        """Apply a High Quality 3D Denoiser.

        Args:
            luma_spatial (float): spatial luma strength (from 0 to DBL_MAX)

                Defaults to 0.
            chroma_spatial (float): spatial chroma strength (from 0 to DBL_MAX)

                Defaults to 0.
            luma_tmp (float): temporal luma strength (from 0 to DBL_MAX)

                Defaults to 0.
            chroma_tmp (float): temporal chroma strength (from 0 to DBL_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hqdn3d",
            inputs=[self],
            named_arguments={
                "luma_spatial": luma_spatial,
                "chroma_spatial": chroma_spatial,
                "luma_tmp": luma_tmp,
                "chroma_tmp": chroma_tmp,
            },
        )[0]

    def hqx(self, n: int | None = None) -> "Stream":
        """Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

        Args:
            n (int): set scale factor (from 2 to 4)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hqx",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def hstack(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        shortest: bool | None = None,
    ) -> "Stream":
        """Stack video inputs horizontally.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): set number of inputs (from 2 to INT_MAX)

                Defaults to 2.
            shortest (bool): force termination when the shortest input terminates

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "shortest": shortest,
            },
        )[0]

    def hsvhold(
        self,
        hue: float | None = None,
        sat: float | None = None,
        val: float | None = None,
        similarity: float | None = None,
        blend: float | None = None,
    ) -> "Stream":
        """Turns a certain HSV range into gray.

        Args:
            hue (float): set the hue value (from -360 to 360)

                Defaults to 0.
            sat (float): set the saturation value (from -1 to 1)

                Defaults to 0.
            val (float): set the value value (from -1 to 1)

                Defaults to 0.
            similarity (float): set the hsvhold similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the hsvhold blend value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hsvhold",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def hsvkey(
        self,
        hue: float | None = None,
        sat: float | None = None,
        val: float | None = None,
        similarity: float | None = None,
        blend: float | None = None,
    ) -> "Stream":
        """Turns a certain HSV range into transparency. Operates on YUV colors.

        Args:
            hue (float): set the hue value (from -360 to 360)

                Defaults to 0.
            sat (float): set the saturation value (from -1 to 1)

                Defaults to 0.
            val (float): set the value value (from -1 to 1)

                Defaults to 0.
            similarity (float): set the hsvkey similarity value (from 1e-05 to 1)

                Defaults to 0.01.
            blend (float): set the hsvkey blend value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hsvkey",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "sat": sat,
                "val": val,
                "similarity": similarity,
                "blend": blend,
            },
        )[0]

    def hue(
        self,
        h: str | None = None,
        s: str | None = None,
        H: str | None = None,
        b: str | None = None,
    ) -> "Stream":
        """Adjust the hue and saturation of the input video.

        Args:
            h (str): set the hue angle degrees expression

            s (str): set the saturation expression

                Defaults to 1.
            H (str): set the hue angle radians expression

            b (str): set the brightness expression

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hue",
            inputs=[self],
            named_arguments={
                "h": h,
                "s": s,
                "H": H,
                "b": b,
            },
        )[0]

    def huesaturation(
        self,
        hue: float | None = None,
        saturation: float | None = None,
        intensity: float | None = None,
        colors: Literal["r", "y", "g", "c", "b", "m", "a"] | None = None,
        strength: float | None = None,
        rw: float | None = None,
        gw: float | None = None,
        bw: float | None = None,
        lightness: bool | None = None,
    ) -> "Stream":
        """Apply hue-saturation-intensity adjustments.

        Args:
            hue (float): set the hue shift (from -180 to 180)

                Defaults to 0.
            saturation (float): set the saturation shift (from -1 to 1)

                Defaults to 0.
            intensity (float): set the intensity shift (from -1 to 1)

                Defaults to 0.
            colors (str): set colors range

                Allowed values:
                    * r: reds
                    * y: yellows
                    * g: greens
                    * c: cyans
                    * b: blues
                    * m: magentas
                    * a: all colors

                Defaults to r+y+g+c+b+m+a.
            strength (float): set the filtering strength (from 0 to 100)

                Defaults to 1.
            rw (float): set the red weight (from 0 to 1)

                Defaults to 0.333.
            gw (float): set the green weight (from 0 to 1)

                Defaults to 0.334.
            bw (float): set the blue weight (from 0 to 1)

                Defaults to 0.333.
            lightness (bool): set the preserve lightness

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="huesaturation",
            inputs=[self],
            named_arguments={
                "hue": hue,
                "saturation": saturation,
                "intensity": intensity,
                "colors": colors,
                "strength": strength,
                "rw": rw,
                "gw": gw,
                "bw": bw,
                "lightness": lightness,
            },
        )[0]

    def hwdownload(
        self,
    ) -> "Stream":
        """Download a hardware frame to a normal frame

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hwdownload", inputs=[self], named_arguments={}
        )[0]

    def hwmap(
        self,
        mode: Literal["read", "write", "overwrite", "direct"] | None = None,
        derive_device: str | None = None,
        reverse: int | None = None,
    ) -> "Stream":
        """Map hardware frames

        Args:
            mode (str): Frame mapping mode

                Allowed values:
                    * read: should be readable
                    * write: should be writeable
                    * overwrite: will always overwrite the entire frame
                    * direct: should not involve any copying

                Defaults to read+write.
            derive_device (str): Derive a new device of this type

            reverse (int): Map in reverse (create and allocate in the sink) (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hwmap",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "derive_device": derive_device,
                "reverse": reverse,
            },
        )[0]

    def hwupload(self, derive_device: str | None = None) -> "Stream":
        """Upload a normal frame to a hardware frame

        Args:
            derive_device (str): Derive a new device of this type


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hwupload",
            inputs=[self],
            named_arguments={
                "derive_device": derive_device,
            },
        )[0]

    def hysteresis(
        self,
        alt_stream: "Stream",
        planes: int | None = None,
        threshold: int | None = None,
    ) -> "Stream":
        """Grow first stream into second stream by connecting components.

        Args:
            alt_stream (Stream): Input video stream.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.
            threshold (int): set threshold (from 0 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="hysteresis",
            inputs=[self, alt_stream],
            named_arguments={
                "planes": planes,
                "threshold": threshold,
            },
        )[0]

    def identity(self, reference_stream: "Stream") -> "Stream":
        """Calculate the Identity between two video streams.

        Args:
            reference_stream (Stream): Input video stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="identity", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def idet(
        self,
        intl_thres: float | None = None,
        prog_thres: float | None = None,
        rep_thres: float | None = None,
        half_life: float | None = None,
        analyze_interlaced_flag: int | None = None,
    ) -> "Stream":
        """Interlace detect Filter.

        Args:
            intl_thres (float): set interlacing threshold (from -1 to FLT_MAX)

                Defaults to 1.04.
            prog_thres (float): set progressive threshold (from -1 to FLT_MAX)

                Defaults to 1.5.
            rep_thres (float): set repeat threshold (from -1 to FLT_MAX)

                Defaults to 3.
            half_life (float): half life of cumulative statistics (from -1 to INT_MAX)

                Defaults to 0.
            analyze_interlaced_flag (int): set number of frames to use to determine if the interlace flag is accurate (from 0 to INT_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="idet",
            inputs=[self],
            named_arguments={
                "intl_thres": intl_thres,
                "prog_thres": prog_thres,
                "rep_thres": rep_thres,
                "half_life": half_life,
                "analyze_interlaced_flag": analyze_interlaced_flag,
            },
        )[0]

    def il(
        self,
        luma_mode: Literal["none", "interleave", "i", "deinterleave", "d"]
        | int
        | None = None,
        l: Literal["none", "interleave", "i", "deinterleave", "d"] | int | None = None,
        chroma_mode: Literal["none", "interleave", "i", "deinterleave", "d"]
        | int
        | None = None,
        c: Literal["none", "interleave", "i", "deinterleave", "d"] | int | None = None,
        alpha_mode: Literal["none", "interleave", "i", "deinterleave", "d"]
        | int
        | None = None,
        a: Literal["none", "interleave", "i", "deinterleave", "d"] | int | None = None,
        luma_swap: bool | None = None,
        ls: bool | None = None,
        chroma_swap: bool | None = None,
        cs: bool | None = None,
        alpha_swap: bool | None = None,
        as_: bool | None = None,
    ) -> "Stream":
        """Deinterleave or interleave fields.

        Args:
            luma_mode (int | str): select luma mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            l (int | str): select luma mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            chroma_mode (int | str): select chroma mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            c (int | str): select chroma mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            alpha_mode (int | str): select alpha mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            a (int | str): select alpha mode (from 0 to 2)

                Allowed values:
                    * none
                    * interleave
                    * i
                    * deinterleave
                    * d

                Defaults to none.
            luma_swap (bool): swap luma fields

                Defaults to false.
            ls (bool): swap luma fields

                Defaults to false.
            chroma_swap (bool): swap chroma fields

                Defaults to false.
            cs (bool): swap chroma fields

                Defaults to false.
            alpha_swap (bool): swap alpha fields

                Defaults to false.
            as_ (bool): swap alpha fields

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="il",
            inputs=[self],
            named_arguments={
                "luma_mode": luma_mode,
                "l": l,
                "chroma_mode": chroma_mode,
                "c": c,
                "alpha_mode": alpha_mode,
                "a": a,
                "luma_swap": luma_swap,
                "ls": ls,
                "chroma_swap": chroma_swap,
                "cs": cs,
                "alpha_swap": alpha_swap,
                "as": as_,
            },
        )[0]

    def inflate(
        self,
        threshold0: int | None = None,
        threshold1: int | None = None,
        threshold2: int | None = None,
        threshold3: int | None = None,
    ) -> "Stream":
        """Apply inflate effect.

        Args:
            threshold0 (int): set threshold for 1st plane (from 0 to 65535)

                Defaults to 65535.
            threshold1 (int): set threshold for 2nd plane (from 0 to 65535)

                Defaults to 65535.
            threshold2 (int): set threshold for 3rd plane (from 0 to 65535)

                Defaults to 65535.
            threshold3 (int): set threshold for 4th plane (from 0 to 65535)

                Defaults to 65535.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="inflate",
            inputs=[self],
            named_arguments={
                "threshold0": threshold0,
                "threshold1": threshold1,
                "threshold2": threshold2,
                "threshold3": threshold3,
            },
        )[0]

    def interlace(
        self,
        scan: Literal["tff", "bff"] | int | None = None,
        lowpass: Literal["off", "linear", "complex"] | int | None = None,
    ) -> "Stream":
        """Convert progressive video into interlaced.

        Args:
            scan (int | str): scanning mode (from 0 to 1)

                Allowed values:
                    * tff: top field first
                    * bff: bottom field first

                Defaults to tff.
            lowpass (int | str): set vertical low-pass filter (from 0 to 2)

                Allowed values:
                    * off: disable vertical low-pass filter
                    * linear: linear vertical low-pass filter
                    * complex: complex vertical low-pass filter

                Defaults to linear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="interlace",
            inputs=[self],
            named_arguments={
                "scan": scan,
                "lowpass": lowpass,
            },
        )[0]

    def interleave(
        self,
        *streams: "Stream",
        nb_inputs: int | None = None,
        n: int | None = None,
        duration: Literal["longest", "shortest", "first"] | int | None = None,
    ) -> "Stream":
        """Temporally interleave video inputs.

        Args:
            *streams (Stream): One or more input streams.
            nb_inputs (int): set number of inputs (from 1 to INT_MAX)

                Defaults to 2.
            n (int): set number of inputs (from 1 to INT_MAX)

                Defaults to 2.
            duration (int | str): how to determine the end-of-stream (from 0 to 2)

                Allowed values:
                    * longest: Duration of longest input
                    * shortest: Duration of shortest input
                    * first: Duration of first input

                Defaults to longest.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="interleave",
            inputs=[self, *streams],
            named_arguments={
                "nb_inputs": nb_inputs,
                "n": n,
                "duration": duration,
            },
        )[0]

    def join(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        channel_layout: str | None = None,
        map: str | None = None,
    ) -> "Stream":
        """Join multiple audio streams into multi-channel output.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): Number of input streams. (from 1 to INT_MAX)

                Defaults to 2.
            channel_layout (str): Channel layout of the output stream.

                Defaults to stereo.
            map (str): A comma-separated list of channels maps in the format 'input_stream.input_channel-output_channel.


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="join",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "channel_layout": channel_layout,
                "map": map,
            },
        )[0]

    def kerndeint(
        self,
        thresh: int | None = None,
        map: bool | None = None,
        order: bool | None = None,
        sharp: bool | None = None,
        twoway: bool | None = None,
    ) -> "Stream":
        """Apply kernel deinterlacing to the input.

        Args:
            thresh (int): set the threshold (from 0 to 255)

                Defaults to 10.
            map (bool): set the map

                Defaults to false.
            order (bool): set the order

                Defaults to false.
            sharp (bool): set sharpening

                Defaults to false.
            twoway (bool): set twoway

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="kerndeint",
            inputs=[self],
            named_arguments={
                "thresh": thresh,
                "map": map,
                "order": order,
                "sharp": sharp,
                "twoway": twoway,
            },
        )[0]

    def kirsch(
        self,
        planes: int | None = None,
        scale: float | None = None,
        delta: float | None = None,
    ) -> "Stream":
        """Apply kirsch operator.

        Args:
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            scale (float): set scale (from 0 to 65535)

                Defaults to 1.
            delta (float): set delta (from -65535 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="kirsch",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def lagfun(self, decay: float | None = None, planes: str | None = None) -> "Stream":
        """Slowly update darker pixels.

        Args:
            decay (float): set decay (from 0 to 1)

                Defaults to 0.95.
            planes (str): set what planes to filter

                Defaults to F.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lagfun",
            inputs=[self],
            named_arguments={
                "decay": decay,
                "planes": planes,
            },
        )[0]

    def latency(
        self,
    ) -> "Stream":
        """Report video filtering latency.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="latency", inputs=[self], named_arguments={}
        )[0]

    def lenscorrection(
        self,
        cx: float | None = None,
        cy: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        i: Literal["nearest", "bilinear"] | int | None = None,
        fc: str | None = None,
    ) -> "Stream":
        """Rectify the image by correcting for lens distortion.

        Args:
            cx (float): set relative center x (from 0 to 1)

                Defaults to 0.5.
            cy (float): set relative center y (from 0 to 1)

                Defaults to 0.5.
            k1 (float): set quadratic distortion factor (from -1 to 1)

                Defaults to 0.
            k2 (float): set double quadratic distortion factor (from -1 to 1)

                Defaults to 0.
            i (int | str): set interpolation type (from 0 to 64)

                Allowed values:
                    * nearest: nearest neighbour
                    * bilinear: bilinear

                Defaults to nearest.
            fc (str): set the color of the unmapped pixels

                Defaults to black@0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lenscorrection",
            inputs=[self],
            named_arguments={
                "cx": cx,
                "cy": cy,
                "k1": k1,
                "k2": k2,
                "i": i,
                "fc": fc,
            },
        )[0]

    def libvmaf(
        self,
        reference_stream: "Stream",
        log_path: str | None = None,
        log_fmt: str | None = None,
        pool: str | None = None,
        n_threads: int | None = None,
        n_subsample: int | None = None,
        model: str | None = None,
        feature: str | None = None,
    ) -> "Stream":
        """Calculate the VMAF between two video streams.

        Args:
            reference_stream (Stream): Input video stream.
            log_path (str): Set the file path to be used to write log.

            log_fmt (str): Set the format of the log (csv, json, xml, or sub).

                Defaults to xml.
            pool (str): Set the pool method to be used for computing vmaf.

            n_threads (int): Set number of threads to be used when computing vmaf. (from 0 to UINT32_MAX)

                Defaults to 0.
            n_subsample (int): Set interval for frame subsampling used when computing vmaf. (from 1 to UINT32_MAX)

                Defaults to 1.
            model (str): Set the model to be used for computing vmaf.

                Defaults to version=vmaf_v0.6.1.
            feature (str): Set the feature to be used for computing vmaf.


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="libvmaf",
            inputs=[self, reference_stream],
            named_arguments={
                "log_path": log_path,
                "log_fmt": log_fmt,
                "pool": pool,
                "n_threads": n_threads,
                "n_subsample": n_subsample,
                "model": model,
                "feature": feature,
            },
        )[0]

    def limitdiff(
        self,
        *streams: "Stream",
        threshold: float | None = None,
        elasticity: float | None = None,
        reference: bool | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply filtering with limiting difference.

        Args:
            *streams (Stream): One or more input streams.
            threshold (float): set the threshold (from 0 to 1)

                Defaults to 0.00392157.
            elasticity (float): set the elasticity (from 0 to 10)

                Defaults to 2.
            reference (bool): enable reference stream

                Defaults to false.
            planes (int): set the planes to filter (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="limitdiff",
            inputs=[self, *streams],
            named_arguments={
                "threshold": threshold,
                "elasticity": elasticity,
                "reference": reference,
                "planes": planes,
            },
        )[0]

    def limiter(
        self, min: int | None = None, max: int | None = None, planes: int | None = None
    ) -> "Stream":
        """Limit pixels components to the specified range.

        Args:
            min (int): set min value (from 0 to 65535)

                Defaults to 0.
            max (int): set max value (from 0 to 65535)

                Defaults to 65535.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="limiter",
            inputs=[self],
            named_arguments={
                "min": min,
                "max": max,
                "planes": planes,
            },
        )[0]

    def loop(
        self,
        loop: int | None = None,
        size: str | None = None,
        start: str | None = None,
        time: str | None = None,
    ) -> "Stream":
        """Loop video frames.

        Args:
            loop (int): number of loops (from -1 to INT_MAX)

                Defaults to 0.
            size (str): max number of frames to loop (from 0 to 32767)

                Defaults to 0.
            start (str): set the loop start frame (from -1 to I64_MAX)

                Defaults to 0.
            time (str): set the loop start time

                Defaults to INT64_MAX.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="loop",
            inputs=[self],
            named_arguments={
                "loop": loop,
                "size": size,
                "start": start,
                "time": time,
            },
        )[0]

    def loudnorm(
        self,
        I: float | None = None,
        i: float | None = None,
        LRA: float | None = None,
        lra: float | None = None,
        TP: float | None = None,
        tp: float | None = None,
        measured_I: float | None = None,
        measured_i: float | None = None,
        measured_LRA: float | None = None,
        measured_lra: float | None = None,
        measured_TP: float | None = None,
        measured_tp: float | None = None,
        measured_thresh: float | None = None,
        offset: float | None = None,
        linear: bool | None = None,
        dual_mono: bool | None = None,
        print_format: Literal["none", "json", "summary"] | int | None = None,
    ) -> "Stream":
        """EBU R128 loudness normalization

        Args:
            I (float): set integrated loudness target (from -70 to -5)

                Defaults to -24.
            i (float): set integrated loudness target (from -70 to -5)

                Defaults to -24.
            LRA (float): set loudness range target (from 1 to 50)

                Defaults to 7.
            lra (float): set loudness range target (from 1 to 50)

                Defaults to 7.
            TP (float): set maximum true peak (from -9 to 0)

                Defaults to -2.
            tp (float): set maximum true peak (from -9 to 0)

                Defaults to -2.
            measured_I (float): measured IL of input file (from -99 to 0)

                Defaults to 0.
            measured_i (float): measured IL of input file (from -99 to 0)

                Defaults to 0.
            measured_LRA (float): measured LRA of input file (from 0 to 99)

                Defaults to 0.
            measured_lra (float): measured LRA of input file (from 0 to 99)

                Defaults to 0.
            measured_TP (float): measured true peak of input file (from -99 to 99)

                Defaults to 99.
            measured_tp (float): measured true peak of input file (from -99 to 99)

                Defaults to 99.
            measured_thresh (float): measured threshold of input file (from -99 to 0)

                Defaults to -70.
            offset (float): set offset gain (from -99 to 99)

                Defaults to 0.
            linear (bool): normalize linearly if possible

                Defaults to true.
            dual_mono (bool): treat mono input as dual-mono

                Defaults to false.
            print_format (int | str): set print format for stats (from 0 to 2)

                Allowed values:
                    * none
                    * json
                    * summary

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="loudnorm",
            inputs=[self],
            named_arguments={
                "I": I,
                "i": i,
                "LRA": LRA,
                "lra": lra,
                "TP": TP,
                "tp": tp,
                "measured_I": measured_I,
                "measured_i": measured_i,
                "measured_LRA": measured_LRA,
                "measured_lra": measured_lra,
                "measured_TP": measured_TP,
                "measured_tp": measured_tp,
                "measured_thresh": measured_thresh,
                "offset": offset,
                "linear": linear,
                "dual_mono": dual_mono,
                "print_format": print_format,
            },
        )[0]

    def lowpass(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a low-pass filter with 3dB point frequency.

        Args:
            frequency (float): set frequency (from 0 to 999999)

                Defaults to 500.
            f (float): set frequency (from 0 to 999999)

                Defaults to 500.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.707.
            w (float): set width (from 0 to 99999)

                Defaults to 0.707.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lowpass",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def lowshelf(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a low shelf filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 100.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 100.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lowshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def lumakey(
        self,
        threshold: float | None = None,
        tolerance: float | None = None,
        softness: float | None = None,
    ) -> "Stream":
        """Turns a certain luma into transparency.

        Args:
            threshold (float): set the threshold value (from 0 to 1)

                Defaults to 0.
            tolerance (float): set the tolerance value (from 0 to 1)

                Defaults to 0.01.
            softness (float): set the softness value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lumakey",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "tolerance": tolerance,
                "softness": softness,
            },
        )[0]

    def lut(
        self,
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
        y: str | None = None,
        u: str | None = None,
        v: str | None = None,
        r: str | None = None,
        g: str | None = None,
        b: str | None = None,
        a: str | None = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the RGB/YUV input video.

        Args:
            c0 (str): set component #0 expression

                Defaults to clipval.
            c1 (str): set component #1 expression

                Defaults to clipval.
            c2 (str): set component #2 expression

                Defaults to clipval.
            c3 (str): set component #3 expression

                Defaults to clipval.
            y (str): set Y expression

                Defaults to clipval.
            u (str): set U expression

                Defaults to clipval.
            v (str): set V expression

                Defaults to clipval.
            r (str): set R expression

                Defaults to clipval.
            g (str): set G expression

                Defaults to clipval.
            b (str): set B expression

                Defaults to clipval.
            a (str): set A expression

                Defaults to clipval.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lut",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def lut1d(
        self,
        file: str | None = None,
        interp: Literal["nearest", "linear", "cosine", "cubic", "spline"]
        | int
        | None = None,
    ) -> "Stream":
        """Adjust colors using a 1D LUT.

        Args:
            file (str): set 1D LUT file name

            interp (int | str): select interpolation mode (from 0 to 4)

                Allowed values:
                    * nearest: use values from the nearest defined points
                    * linear: use values from the linear interpolation
                    * cosine: use values from the cosine interpolation
                    * cubic: use values from the cubic interpolation
                    * spline: use values from the spline interpolation

                Defaults to linear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lut1d",
            inputs=[self],
            named_arguments={
                "file": file,
                "interp": interp,
            },
        )[0]

    def lut2(
        self,
        srcy_stream: "Stream",
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
        d: int | None = None,
    ) -> "Stream":
        """Compute and apply a lookup table from two video inputs.

        Args:
            srcy_stream (Stream): Input video stream.
            c0 (str): set component #0 expression

                Defaults to x.
            c1 (str): set component #1 expression

                Defaults to x.
            c2 (str): set component #2 expression

                Defaults to x.
            c3 (str): set component #3 expression

                Defaults to x.
            d (int): set output depth (from 0 to 16)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lut2",
            inputs=[self, srcy_stream],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "d": d,
            },
        )[0]

    def lut3d(
        self,
        file: str | None = None,
        clut: Literal["first", "all"] | int | None = None,
        interp: Literal["nearest", "trilinear", "tetrahedral", "pyramid", "prism"]
        | int
        | None = None,
    ) -> "Stream":
        """Adjust colors using a 3D LUT.

        Args:
            file (str): set 3D LUT file name

            clut (int | str): when to process CLUT (from 0 to 1)

                Allowed values:
                    * first: process only first CLUT, ignore rest
                    * all: process all CLUTs

                Defaults to all.
            interp (int | str): select interpolation mode (from 0 to 4)

                Allowed values:
                    * nearest: use values from the nearest defined points
                    * trilinear: interpolate values using the 8 points defining a cube
                    * tetrahedral: interpolate values using a tetrahedron
                    * pyramid: interpolate values using a pyramid
                    * prism: interpolate values using a prism

                Defaults to tetrahedral.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lut3d",
            inputs=[self],
            named_arguments={
                "file": file,
                "clut": clut,
                "interp": interp,
            },
        )[0]

    def lutrgb(
        self,
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
        y: str | None = None,
        u: str | None = None,
        v: str | None = None,
        r: str | None = None,
        g: str | None = None,
        b: str | None = None,
        a: str | None = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the RGB input video.

        Args:
            c0 (str): set component #0 expression

                Defaults to clipval.
            c1 (str): set component #1 expression

                Defaults to clipval.
            c2 (str): set component #2 expression

                Defaults to clipval.
            c3 (str): set component #3 expression

                Defaults to clipval.
            y (str): set Y expression

                Defaults to clipval.
            u (str): set U expression

                Defaults to clipval.
            v (str): set V expression

                Defaults to clipval.
            r (str): set R expression

                Defaults to clipval.
            g (str): set G expression

                Defaults to clipval.
            b (str): set B expression

                Defaults to clipval.
            a (str): set A expression

                Defaults to clipval.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lutrgb",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def lutyuv(
        self,
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
        y: str | None = None,
        u: str | None = None,
        v: str | None = None,
        r: str | None = None,
        g: str | None = None,
        b: str | None = None,
        a: str | None = None,
    ) -> "Stream":
        """Compute and apply a lookup table to the YUV input video.

        Args:
            c0 (str): set component #0 expression

                Defaults to clipval.
            c1 (str): set component #1 expression

                Defaults to clipval.
            c2 (str): set component #2 expression

                Defaults to clipval.
            c3 (str): set component #3 expression

                Defaults to clipval.
            y (str): set Y expression

                Defaults to clipval.
            u (str): set U expression

                Defaults to clipval.
            v (str): set V expression

                Defaults to clipval.
            r (str): set R expression

                Defaults to clipval.
            g (str): set G expression

                Defaults to clipval.
            b (str): set B expression

                Defaults to clipval.
            a (str): set A expression

                Defaults to clipval.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="lutyuv",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "y": y,
                "u": u,
                "v": v,
                "r": r,
                "g": g,
                "b": b,
                "a": a,
            },
        )[0]

    def maskedclamp(
        self,
        dark_stream: "Stream",
        bright_stream: "Stream",
        undershoot: int | None = None,
        overshoot: int | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Clamp first stream with second stream and third stream.

        Args:
            dark_stream (Stream): Input video stream.
            bright_stream (Stream): Input video stream.
            undershoot (int): set undershoot (from 0 to 65535)

                Defaults to 0.
            overshoot (int): set overshoot (from 0 to 65535)

                Defaults to 0.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskedclamp",
            inputs=[self, dark_stream, bright_stream],
            named_arguments={
                "undershoot": undershoot,
                "overshoot": overshoot,
                "planes": planes,
            },
        )[0]

    def maskedmax(
        self,
        filter1_stream: "Stream",
        filter2_stream: "Stream",
        planes: int | None = None,
    ) -> "Stream":
        """Apply filtering with maximum difference of two streams.

        Args:
            filter1_stream (Stream): Input video stream.
            filter2_stream (Stream): Input video stream.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskedmax",
            inputs=[self, filter1_stream, filter2_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedmerge(
        self, overlay_stream: "Stream", mask_stream: "Stream", planes: int | None = None
    ) -> "Stream":
        """Merge first stream with second stream using third stream as mask.

        Args:
            overlay_stream (Stream): Input video stream.
            mask_stream (Stream): Input video stream.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskedmerge",
            inputs=[self, overlay_stream, mask_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedmin(
        self,
        filter1_stream: "Stream",
        filter2_stream: "Stream",
        planes: int | None = None,
    ) -> "Stream":
        """Apply filtering with minimum difference of two streams.

        Args:
            filter1_stream (Stream): Input video stream.
            filter2_stream (Stream): Input video stream.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskedmin",
            inputs=[self, filter1_stream, filter2_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def maskedthreshold(
        self,
        reference_stream: "Stream",
        threshold: int | None = None,
        planes: int | None = None,
        mode: Literal["abs", "diff"] | int | None = None,
    ) -> "Stream":
        """Pick pixels comparing absolute difference of two streams with threshold.

        Args:
            reference_stream (Stream): Input video stream.
            threshold (int): set threshold (from 0 to 65535)

                Defaults to 1.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * abs
                    * diff

                Defaults to abs.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskedthreshold",
            inputs=[self, reference_stream],
            named_arguments={
                "threshold": threshold,
                "planes": planes,
                "mode": mode,
            },
        )[0]

    def maskfun(
        self,
        low: int | None = None,
        high: int | None = None,
        planes: int | None = None,
        fill: int | None = None,
        sum: int | None = None,
    ) -> "Stream":
        """Create Mask.

        Args:
            low (int): set low threshold (from 0 to 65535)

                Defaults to 10.
            high (int): set high threshold (from 0 to 65535)

                Defaults to 10.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.
            fill (int): set fill value (from 0 to 65535)

                Defaults to 0.
            sum (int): set sum value (from 0 to 65535)

                Defaults to 10.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="maskfun",
            inputs=[self],
            named_arguments={
                "low": low,
                "high": high,
                "planes": planes,
                "fill": fill,
                "sum": sum,
            },
        )[0]

    def mcdeint(
        self,
        mode: Literal["fast", "medium", "slow", "extra_slow"] | int | None = None,
        parity: Literal["tff", "bff"] | int | None = None,
        qp: int | None = None,
    ) -> "Stream":
        """Apply motion compensating deinterlacing.

        Args:
            mode (int | str): set mode (from 0 to 3)

                Allowed values:
                    * fast
                    * medium
                    * slow
                    * extra_slow

                Defaults to fast.
            parity (int | str): set the assumed picture field parity (from -1 to 1)

                Allowed values:
                    * tff: assume top field first
                    * bff: assume bottom field first

                Defaults to bff.
            qp (int): set qp (from INT_MIN to INT_MAX)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mcdeint",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "qp": qp,
            },
        )[0]

    def mcompand(self, args: str | None = None) -> "Stream":
        """Multiband Compress or expand audio dynamic range.

        Args:
            args (str): set parameters for each band

                Defaults to 0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mcompand",
            inputs=[self],
            named_arguments={
                "args": args,
            },
        )[0]

    def median(
        self,
        radius: int | None = None,
        planes: int | None = None,
        radiusV: int | None = None,
        percentile: float | None = None,
    ) -> "Stream":
        """Apply Median filter.

        Args:
            radius (int): set median radius (from 1 to 127)

                Defaults to 1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            radiusV (int): set median vertical radius (from 0 to 127)

                Defaults to 0.
            percentile (float): set median percentile (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="median",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "planes": planes,
                "radiusV": radiusV,
                "percentile": percentile,
            },
        )[0]

    def mergeplanes(
        self,
        *streams: "Stream",
        mapping: int | None = None,
        format: str | None = None,
        map0s: int | None = None,
        map0p: int | None = None,
        map1s: int | None = None,
        map1p: int | None = None,
        map2s: int | None = None,
        map2p: int | None = None,
        map3s: int | None = None,
        map3p: int | None = None,
    ) -> "Stream":
        """Merge planes.

        Args:
            *streams (Stream): One or more input streams.
            mapping (int): set input to output plane mapping (from -1 to 8.58993e+08)

                Defaults to -1.
            format (str): set output pixel format

                Defaults to yuva444p.
            map0s (int): set 1st input to output stream mapping (from 0 to 3)

                Defaults to 0.
            map0p (int): set 1st input to output plane mapping (from 0 to 3)

                Defaults to 0.
            map1s (int): set 2nd input to output stream mapping (from 0 to 3)

                Defaults to 0.
            map1p (int): set 2nd input to output plane mapping (from 0 to 3)

                Defaults to 0.
            map2s (int): set 3rd input to output stream mapping (from 0 to 3)

                Defaults to 0.
            map2p (int): set 3rd input to output plane mapping (from 0 to 3)

                Defaults to 0.
            map3s (int): set 4th input to output stream mapping (from 0 to 3)

                Defaults to 0.
            map3p (int): set 4th input to output plane mapping (from 0 to 3)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mergeplanes",
            inputs=[self, *streams],
            named_arguments={
                "mapping": mapping,
                "format": format,
                "map0s": map0s,
                "map0p": map0p,
                "map1s": map1s,
                "map1p": map1p,
                "map2s": map2s,
                "map2p": map2p,
                "map3s": map3s,
                "map3p": map3p,
            },
        )[0]

    def mestimate(
        self,
        method: Literal[
            "esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"
        ]
        | int
        | None = None,
        mb_size: int | None = None,
        search_param: int | None = None,
    ) -> "Stream":
        """Generate motion vectors.

        Args:
            method (int | str): motion estimation method (from 1 to 9)

                Allowed values:
                    * esa: exhaustive search
                    * tss: three step search
                    * tdls: two dimensional logarithmic search
                    * ntss: new three step search
                    * fss: four step search
                    * ds: diamond search
                    * hexbs: hexagon-based search
                    * epzs: enhanced predictive zonal search
                    * umh: uneven multi-hexagon search

                Defaults to esa.
            mb_size (int): macroblock size (from 8 to INT_MAX)

                Defaults to 16.
            search_param (int): search parameter (from 4 to INT_MAX)

                Defaults to 7.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mestimate",
            inputs=[self],
            named_arguments={
                "method": method,
                "mb_size": mb_size,
                "search_param": search_param,
            },
        )[0]

    def metadata(
        self,
        mode: Literal["select", "add", "modify", "delete", "print"] | int | None = None,
        key: str | None = None,
        value: str | None = None,
        function: Literal[
            "same_str", "starts_with", "less", "equal", "greater", "expr", "ends_with"
        ]
        | int
        | None = None,
        expr: str | None = None,
        file: str | None = None,
        direct: bool | None = None,
    ) -> "Stream":
        """Manipulate video frame metadata.

        Args:
            mode (int | str): set a mode of operation (from 0 to 4)

                Allowed values:
                    * select: select frame
                    * add: add new metadata
                    * modify: modify metadata
                    * delete: delete metadata
                    * print: print metadata

                Defaults to select.
            key (str): set metadata key

            value (str): set metadata value

            function (int | str): function for comparing values (from 0 to 6)

                Allowed values:
                    * same_str
                    * starts_with
                    * less
                    * equal
                    * greater
                    * expr
                    * ends_with

                Defaults to same_str.
            expr (str): set expression for expr function

            file (str): set file where to print metadata information

            direct (bool): reduce buffering when printing to user-set file or pipe

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="metadata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "key": key,
                "value": value,
                "function": function,
                "expr": expr,
                "file": file,
                "direct": direct,
            },
        )[0]

    def midequalizer(self, in1_stream: "Stream", planes: int | None = None) -> "Stream":
        """Apply Midway Equalization.

        Args:
            in1_stream (Stream): Input video stream.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="midequalizer",
            inputs=[self, in1_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def minterpolate(
        self,
        fps: str | None = None,
        mi_mode: Literal["dup", "blend", "mci"] | int | None = None,
        mc_mode: Literal["obmc", "aobmc"] | int | None = None,
        me_mode: Literal["bidir", "bilat"] | int | None = None,
        me: Literal["esa", "tss", "tdls", "ntss", "fss", "ds", "hexbs", "epzs", "umh"]
        | int
        | None = None,
        mb_size: int | None = None,
        search_param: int | None = None,
        vsbmc: int | None = None,
        scd: Literal["none", "fdiff"] | int | None = None,
        scd_threshold: float | None = None,
    ) -> "Stream":
        """Frame rate conversion using Motion Interpolation.

        Args:
            fps (str): output's frame rate

                Defaults to 60.
            mi_mode (int | str): motion interpolation mode (from 0 to 2)

                Allowed values:
                    * dup: duplicate frames
                    * blend: blend frames
                    * mci: motion compensated interpolation

                Defaults to mci.
            mc_mode (int | str): motion compensation mode (from 0 to 1)

                Allowed values:
                    * obmc: overlapped block motion compensation
                    * aobmc: adaptive overlapped block motion compensation

                Defaults to obmc.
            me_mode (int | str): motion estimation mode (from 0 to 1)

                Allowed values:
                    * bidir: bidirectional motion estimation
                    * bilat: bilateral motion estimation

                Defaults to bilat.
            me (int | str): motion estimation method (from 1 to 9)

                Allowed values:
                    * esa: exhaustive search
                    * tss: three step search
                    * tdls: two dimensional logarithmic search
                    * ntss: new three step search
                    * fss: four step search
                    * ds: diamond search
                    * hexbs: hexagon-based search
                    * epzs: enhanced predictive zonal search
                    * umh: uneven multi-hexagon search

                Defaults to epzs.
            mb_size (int): macroblock size (from 4 to 16)

                Defaults to 16.
            search_param (int): search parameter (from 4 to INT_MAX)

                Defaults to 32.
            vsbmc (int): variable-size block motion compensation (from 0 to 1)

                Defaults to 0.
            scd (int | str): scene change detection method (from 0 to 1)

                Allowed values:
                    * none: disable detection
                    * fdiff: frame difference

                Defaults to fdiff.
            scd_threshold (float): scene change threshold (from 0 to 100)

                Defaults to 10.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="minterpolate",
            inputs=[self],
            named_arguments={
                "fps": fps,
                "mi_mode": mi_mode,
                "mc_mode": mc_mode,
                "me_mode": me_mode,
                "me": me,
                "mb_size": mb_size,
                "search_param": search_param,
                "vsbmc": vsbmc,
                "scd": scd,
                "scd_threshold": scd_threshold,
            },
        )[0]

    def mix(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        weights: str | None = None,
        scale: float | None = None,
        planes: str | None = None,
        duration: Literal["longest", "shortest", "first"] | int | None = None,
    ) -> "Stream":
        """Mix video inputs.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): set number of inputs (from 2 to 32767)

                Defaults to 2.
            weights (str): set weight for each input

                Defaults to 1 1.
            scale (float): set scale (from 0 to 32767)

                Defaults to 0.
            planes (str): set what planes to filter

                Defaults to F.
            duration (int | str): how to determine end of stream (from 0 to 2)

                Allowed values:
                    * longest: Duration of longest input
                    * shortest: Duration of shortest input
                    * first: Duration of first input

                Defaults to longest.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mix",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "weights": weights,
                "scale": scale,
                "planes": planes,
                "duration": duration,
            },
        )[0]

    def monochrome(
        self,
        cb: float | None = None,
        cr: float | None = None,
        size: float | None = None,
        high: float | None = None,
    ) -> "Stream":
        """Convert video to gray using custom color filter.

        Args:
            cb (float): set the chroma blue spot (from -1 to 1)

                Defaults to 0.
            cr (float): set the chroma red spot (from -1 to 1)

                Defaults to 0.
            size (float): set the color filter size (from 0.1 to 10)

                Defaults to 1.
            high (float): set the highlights strength (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="monochrome",
            inputs=[self],
            named_arguments={
                "cb": cb,
                "cr": cr,
                "size": size,
                "high": high,
            },
        )[0]

    def morpho(
        self,
        structure_stream: "Stream",
        mode: Literal[
            "erode", "dilate", "open", "close", "gradient", "tophat", "blackhat"
        ]
        | int
        | None = None,
        planes: int | None = None,
        structure: Literal["first", "all"] | int | None = None,
    ) -> "Stream":
        """Apply Morphological filter.

        Args:
            structure_stream (Stream): Input video stream.
            mode (int | str): set morphological transform (from 0 to 6)

                Allowed values:
                    * erode
                    * dilate
                    * open
                    * close
                    * gradient
                    * tophat
                    * blackhat

                Defaults to erode.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 7.
            structure (int | str): when to process structures (from 0 to 1)

                Allowed values:
                    * first: process only first structure, ignore rest
                    * all: process all structure

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="morpho",
            inputs=[self, structure_stream],
            named_arguments={
                "mode": mode,
                "planes": planes,
                "structure": structure,
            },
        )[0]

    def mpdecimate(
        self,
        max: int | None = None,
        keep: int | None = None,
        hi: int | None = None,
        lo: int | None = None,
        frac: float | None = None,
    ) -> "Stream":
        """Remove near-duplicate frames.

        Args:
            max (int): set the maximum number of consecutive dropped frames (positive), or the minimum interval between dropped frames (negative) (from INT_MIN to INT_MAX)

                Defaults to 0.
            keep (int): set the number of similar consecutive frames to be kept before starting to drop similar frames (from 0 to INT_MAX)

                Defaults to 0.
            hi (int): set high dropping threshold (from INT_MIN to INT_MAX)

                Defaults to 768.
            lo (int): set low dropping threshold (from INT_MIN to INT_MAX)

                Defaults to 320.
            frac (float): set fraction dropping threshold (from 0 to 1)

                Defaults to 0.33.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="mpdecimate",
            inputs=[self],
            named_arguments={
                "max": max,
                "keep": keep,
                "hi": hi,
                "lo": lo,
                "frac": frac,
            },
        )[0]

    def msad(self, reference_stream: "Stream") -> "Stream":
        """Calculate the MSAD between two video streams.

        Args:
            reference_stream (Stream): Input video stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="msad", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def multiply(
        self,
        factor_stream: "Stream",
        scale: float | None = None,
        offset: float | None = None,
        planes: str | None = None,
    ) -> "Stream":
        """Multiply first video stream with second video stream.

        Args:
            factor_stream (Stream): Input video stream.
            scale (float): set scale (from 0 to 9)

                Defaults to 1.
            offset (float): set offset (from -1 to 1)

                Defaults to 0.5.
            planes (str): set planes

                Defaults to F.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="multiply",
            inputs=[self, factor_stream],
            named_arguments={
                "scale": scale,
                "offset": offset,
                "planes": planes,
            },
        )[0]

    def negate(
        self,
        components: Literal["y", "u", "v", "r", "g", "b", "a"] | None = None,
        negate_alpha: bool | None = None,
    ) -> "Stream":
        """Negate input video.

        Args:
            components (str): set components to negate

                Allowed values:
                    * y: luma component
                    * u: u component
                    * v: v component
                    * r: red component
                    * g: green component
                    * b: blue component
                    * a: alpha component

                Defaults to y+u+v+r+g+b.
            negate_alpha (bool): No description available.

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="negate",
            inputs=[self],
            named_arguments={
                "components": components,
                "negate_alpha": negate_alpha,
            },
        )[0]

    def nlmeans(
        self,
        s: float | None = None,
        p: int | None = None,
        pc: int | None = None,
        r: int | None = None,
        rc: int | None = None,
    ) -> "Stream":
        """Non-local means denoiser.

        Args:
            s (float): denoising strength (from 1 to 30)

                Defaults to 1.
            p (int): patch size (from 0 to 99)

                Defaults to 7.
            pc (int): patch size for chroma planes (from 0 to 99)

                Defaults to 0.
            r (int): research window (from 0 to 99)

                Defaults to 15.
            rc (int): research window for chroma planes (from 0 to 99)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="nlmeans",
            inputs=[self],
            named_arguments={
                "s": s,
                "p": p,
                "pc": pc,
                "r": r,
                "rc": rc,
            },
        )[0]

    def nnedi(
        self,
        weights: str | None = None,
        deint: Literal["all", "interlaced"] | int | None = None,
        field: Literal["af", "a", "t", "b", "tf", "bf"] | int | None = None,
        planes: int | None = None,
        nsize: Literal["s8x6", "s16x6", "s32x6", "s48x6", "s8x4", "s16x4", "s32x4"]
        | int
        | None = None,
        nns: Literal["n16", "n32", "n64", "n128", "n256"] | int | None = None,
        qual: Literal["fast", "slow"] | int | None = None,
        etype: Literal["a", "abs", "s", "mse"] | int | None = None,
        pscrn: Literal["none", "original", "new", "new2", "new3"] | int | None = None,
    ) -> "Stream":
        """Apply neural network edge directed interpolation intra-only deinterlacer.

        Args:
            weights (str): set weights file

                Defaults to nnedi3_weights.bin.
            deint (int | str): set which frames to deinterlace (from 0 to 1)

                Allowed values:
                    * all: deinterlace all frames
                    * interlaced: only deinterlace frames marked as interlaced

                Defaults to all.
            field (int | str): set mode of operation (from -2 to 3)

                Allowed values:
                    * af: use frame flags, both fields
                    * a: use frame flags, single field
                    * t: use top field only
                    * b: use bottom field only
                    * tf: use both fields, top first
                    * bf: use both fields, bottom first

                Defaults to a.
            planes (int): set which planes to process (from 0 to 15)

                Defaults to 7.
            nsize (int | str): set size of local neighborhood around each pixel, used by the predictor neural network (from 0 to 6)

                Allowed values:
                    * s8x6
                    * s16x6
                    * s32x6
                    * s48x6
                    * s8x4
                    * s16x4
                    * s32x4

                Defaults to s32x4.
            nns (int | str): set number of neurons in predictor neural network (from 0 to 4)

                Allowed values:
                    * n16
                    * n32
                    * n64
                    * n128
                    * n256

                Defaults to n32.
            qual (int | str): set quality (from 1 to 2)

                Allowed values:
                    * fast
                    * slow

                Defaults to fast.
            etype (int | str): set which set of weights to use in the predictor (from 0 to 1)

                Allowed values:
                    * a: weights trained to minimize absolute error
                    * abs: weights trained to minimize absolute error
                    * s: weights trained to minimize squared error
                    * mse: weights trained to minimize squared error

                Defaults to a.
            pscrn (int | str): set prescreening (from 0 to 4)

                Allowed values:
                    * none
                    * original
                    * new
                    * new2
                    * new3

                Defaults to new.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="nnedi",
            inputs=[self],
            named_arguments={
                "weights": weights,
                "deint": deint,
                "field": field,
                "planes": planes,
                "nsize": nsize,
                "nns": nns,
                "qual": qual,
                "etype": etype,
                "pscrn": pscrn,
            },
        )[0]

    def noformat(
        self,
        pix_fmts: str | None = None,
        color_spaces: str | None = None,
        color_ranges: str | None = None,
    ) -> "Stream":
        """Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

        Args:
            pix_fmts (str): A '|'-separated list of pixel formats

            color_spaces (str): A '|'-separated list of color spaces

            color_ranges (str): A '|'-separated list of color ranges


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="noformat",
            inputs=[self],
            named_arguments={
                "pix_fmts": pix_fmts,
                "color_spaces": color_spaces,
                "color_ranges": color_ranges,
            },
        )[0]

    def noise(
        self,
        all_seed: int | None = None,
        all_strength: int | None = None,
        alls: int | None = None,
        all_flags: Literal["a", "p", "t", "u"] | None = None,
        allf: Literal["a", "p", "t", "u"] | None = None,
        c0_seed: int | None = None,
        c0_strength: int | None = None,
        c0s: int | None = None,
        c0_flags: Literal["a", "p", "t", "u"] | None = None,
        c0f: Literal["a", "p", "t", "u"] | None = None,
        c1_seed: int | None = None,
        c1_strength: int | None = None,
        c1s: int | None = None,
        c1_flags: Literal["a", "p", "t", "u"] | None = None,
        c1f: Literal["a", "p", "t", "u"] | None = None,
        c2_seed: int | None = None,
        c2_strength: int | None = None,
        c2s: int | None = None,
        c2_flags: Literal["a", "p", "t", "u"] | None = None,
        c2f: Literal["a", "p", "t", "u"] | None = None,
        c3_seed: int | None = None,
        c3_strength: int | None = None,
        c3s: int | None = None,
        c3_flags: Literal["a", "p", "t", "u"] | None = None,
        c3f: Literal["a", "p", "t", "u"] | None = None,
    ) -> "Stream":
        """Add noise.

        Args:
            all_seed (int): set component #0 noise seed (from -1 to INT_MAX)

                Defaults to -1.
            all_strength (int): set component #0 strength (from 0 to 100)

                Defaults to 0.
            alls (int): set component #0 strength (from 0 to 100)

                Defaults to 0.
            all_flags (str): set component #0 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            allf (str): set component #0 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c0_seed (int): set component #0 noise seed (from -1 to INT_MAX)

                Defaults to -1.
            c0_strength (int): set component #0 strength (from 0 to 100)

                Defaults to 0.
            c0s (int): set component #0 strength (from 0 to 100)

                Defaults to 0.
            c0_flags (str): set component #0 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c0f (str): set component #0 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c1_seed (int): set component #1 noise seed (from -1 to INT_MAX)

                Defaults to -1.
            c1_strength (int): set component #1 strength (from 0 to 100)

                Defaults to 0.
            c1s (int): set component #1 strength (from 0 to 100)

                Defaults to 0.
            c1_flags (str): set component #1 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c1f (str): set component #1 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c2_seed (int): set component #2 noise seed (from -1 to INT_MAX)

                Defaults to -1.
            c2_strength (int): set component #2 strength (from 0 to 100)

                Defaults to 0.
            c2s (int): set component #2 strength (from 0 to 100)

                Defaults to 0.
            c2_flags (str): set component #2 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c2f (str): set component #2 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c3_seed (int): set component #3 noise seed (from -1 to INT_MAX)

                Defaults to -1.
            c3_strength (int): set component #3 strength (from 0 to 100)

                Defaults to 0.
            c3s (int): set component #3 strength (from 0 to 100)

                Defaults to 0.
            c3_flags (str): set component #3 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.
            c3f (str): set component #3 flags

                Allowed values:
                    * a: noise
                    * p: pattern
                    * t: noise
                    * u: noise

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="noise",
            inputs=[self],
            named_arguments={
                "all_seed": all_seed,
                "all_strength": all_strength,
                "alls": alls,
                "all_flags": all_flags,
                "allf": allf,
                "c0_seed": c0_seed,
                "c0_strength": c0_strength,
                "c0s": c0s,
                "c0_flags": c0_flags,
                "c0f": c0f,
                "c1_seed": c1_seed,
                "c1_strength": c1_strength,
                "c1s": c1s,
                "c1_flags": c1_flags,
                "c1f": c1f,
                "c2_seed": c2_seed,
                "c2_strength": c2_strength,
                "c2s": c2s,
                "c2_flags": c2_flags,
                "c2f": c2f,
                "c3_seed": c3_seed,
                "c3_strength": c3_strength,
                "c3s": c3s,
                "c3_flags": c3_flags,
                "c3f": c3f,
            },
        )[0]

    def normalize(
        self,
        blackpt: str | None = None,
        whitept: str | None = None,
        smoothing: int | None = None,
        independence: float | None = None,
        strength: float | None = None,
    ) -> "Stream":
        """Normalize RGB video.

        Args:
            blackpt (str): output color to which darkest input color is mapped

                Defaults to black.
            whitept (str): output color to which brightest input color is mapped

                Defaults to white.
            smoothing (int): amount of temporal smoothing of the input range, to reduce flicker (from 0 to 2.68435e+08)

                Defaults to 0.
            independence (float): proportion of independent to linked channel normalization (from 0 to 1)

                Defaults to 1.
            strength (float): strength of filter, from no effect to full normalization (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="normalize",
            inputs=[self],
            named_arguments={
                "blackpt": blackpt,
                "whitept": whitept,
                "smoothing": smoothing,
                "independence": independence,
                "strength": strength,
            },
        )[0]

    def null(
        self,
    ) -> "Stream":
        """Pass the source unchanged to the output.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="null", inputs=[self], named_arguments={}
        )[0]

    def nullsink(
        self,
    ) -> "SinkNode":
        """Do absolutely nothing with the input video.

        Returns:
            "SinkNode": A SinkNode representing the sink (terminal node).
        """
        return self._apply_sink_filter(
            filter_name="nullsink", inputs=[self], named_arguments={}
        )

    def ocr(
        self,
        datapath: str | None = None,
        language: str | None = None,
        whitelist: str | None = None,
        blacklist: str | None = None,
    ) -> "Stream":
        """Optical Character Recognition.

        Args:
            datapath (str): set datapath

            language (str): set language

                Defaults to eng.
            whitelist (str): set character whitelist

                Defaults to 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,-+_!?"'[]{}()<>|/\=*&%$#@!~.
            blacklist (str): set character blacklist


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ocr",
            inputs=[self],
            named_arguments={
                "datapath": datapath,
                "language": language,
                "whitelist": whitelist,
                "blacklist": blacklist,
            },
        )[0]

    def oscilloscope(
        self,
        x: float | None = None,
        y: float | None = None,
        s: float | None = None,
        t: float | None = None,
        o: float | None = None,
        tx: float | None = None,
        ty: float | None = None,
        tw: float | None = None,
        th: float | None = None,
        c: int | None = None,
        g: bool | None = None,
        st: bool | None = None,
        sc: bool | None = None,
    ) -> "Stream":
        """2D Video Oscilloscope.

        Args:
            x (float): set scope x position (from 0 to 1)

                Defaults to 0.5.
            y (float): set scope y position (from 0 to 1)

                Defaults to 0.5.
            s (float): set scope size (from 0 to 1)

                Defaults to 0.8.
            t (float): set scope tilt (from 0 to 1)

                Defaults to 0.5.
            o (float): set trace opacity (from 0 to 1)

                Defaults to 0.8.
            tx (float): set trace x position (from 0 to 1)

                Defaults to 0.5.
            ty (float): set trace y position (from 0 to 1)

                Defaults to 0.9.
            tw (float): set trace width (from 0.1 to 1)

                Defaults to 0.8.
            th (float): set trace height (from 0.1 to 1)

                Defaults to 0.3.
            c (int): set components to trace (from 0 to 15)

                Defaults to 7.
            g (bool): draw trace grid

                Defaults to true.
            st (bool): draw statistics

                Defaults to true.
            sc (bool): draw scope

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="oscilloscope",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "s": s,
                "t": t,
                "o": o,
                "tx": tx,
                "ty": ty,
                "tw": tw,
                "th": th,
                "c": c,
                "g": g,
                "st": st,
                "sc": sc,
            },
        )[0]

    def overlay(
        self,
        overlay_stream: "Stream",
        x: str | None = None,
        y: str | None = None,
        eof_action: Literal["repeat", "endall", "pass"] | int | None = None,
        eval: Literal["init", "frame"] | int | None = None,
        shortest: bool | None = None,
        format: Literal[
            "yuv420",
            "yuv420p10",
            "yuv422",
            "yuv422p10",
            "yuv444",
            "yuv444p10",
            "rgb",
            "gbrp",
            "auto",
        ]
        | int
        | None = None,
        repeatlast: bool | None = None,
        alpha: Literal["straight", "premultiplied"] | int | None = None,
    ) -> "Stream":
        """Overlay a video source on top of the input.

        Args:
            overlay_stream (Stream): Input video stream.
            x (str): set the x expression

                Defaults to 0.
            y (str): set the y expression

                Defaults to 0.
            eof_action (int | str): Action to take when encountering EOF from secondary input  (from 0 to 2)

                Allowed values:
                    * repeat: Repeat the previous frame.
                    * endall: End both streams.
                    * pass: Pass through the main input.

                Defaults to repeat.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions per-frame

                Defaults to frame.
            shortest (bool): force termination when the shortest input terminates

                Defaults to false.
            format (int | str): set output format (from 0 to 8)

                Allowed values:
                    * yuv420
                    * yuv420p10
                    * yuv422
                    * yuv422p10
                    * yuv444
                    * yuv444p10
                    * rgb
                    * gbrp
                    * auto

                Defaults to yuv420.
            repeatlast (bool): repeat overlay of the last overlay frame

                Defaults to true.
            alpha (int | str): alpha format (from 0 to 1)

                Allowed values:
                    * straight
                    * premultiplied

                Defaults to straight.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="overlay",
            inputs=[self, overlay_stream],
            named_arguments={
                "x": x,
                "y": y,
                "eof_action": eof_action,
                "eval": eval,
                "shortest": shortest,
                "format": format,
                "repeatlast": repeatlast,
                "alpha": alpha,
            },
        )[0]

    def owdenoise(
        self,
        depth: int | None = None,
        luma_strength: float | None = None,
        ls: float | None = None,
        chroma_strength: float | None = None,
        cs: float | None = None,
    ) -> "Stream":
        """Denoise using wavelets.

        Args:
            depth (int): set depth (from 8 to 16)

                Defaults to 8.
            luma_strength (float): set luma strength (from 0 to 1000)

                Defaults to 1.
            ls (float): set luma strength (from 0 to 1000)

                Defaults to 1.
            chroma_strength (float): set chroma strength (from 0 to 1000)

                Defaults to 1.
            cs (float): set chroma strength (from 0 to 1000)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="owdenoise",
            inputs=[self],
            named_arguments={
                "depth": depth,
                "luma_strength": luma_strength,
                "ls": ls,
                "chroma_strength": chroma_strength,
                "cs": cs,
            },
        )[0]

    def pad(
        self,
        width: str | None = None,
        w: str | None = None,
        height: str | None = None,
        h: str | None = None,
        x: str | None = None,
        y: str | None = None,
        color: str | None = None,
        eval: Literal["init", "frame"] | int | None = None,
        aspect: str | None = None,
    ) -> "Stream":
        """Pad the input video.

        Args:
            width (str): set the pad area width expression

                Defaults to iw.
            w (str): set the pad area width expression

                Defaults to iw.
            height (str): set the pad area height expression

                Defaults to ih.
            h (str): set the pad area height expression

                Defaults to ih.
            x (str): set the x offset expression for the input image position

                Defaults to 0.
            y (str): set the y offset expression for the input image position

                Defaults to 0.
            color (str): set the color of the padded area border

                Defaults to black.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions during initialization and per-frame

                Defaults to init.
            aspect (str): pad to fit an aspect instead of a resolution (from 0 to DBL_MAX)

                Defaults to 0/1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pad",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "x": x,
                "y": y,
                "color": color,
                "eval": eval,
                "aspect": aspect,
            },
        )[0]

    def palettegen(
        self,
        max_colors: int | None = None,
        reserve_transparent: bool | None = None,
        transparency_color: str | None = None,
        stats_mode: Literal["full", "diff", "single"] | int | None = None,
    ) -> "Stream":
        """Find the optimal palette for a given stream.

        Args:
            max_colors (int): set the maximum number of colors to use in the palette (from 2 to 256)

                Defaults to 256.
            reserve_transparent (bool): reserve a palette entry for transparency

                Defaults to true.
            transparency_color (str): set a background color for transparency

                Defaults to lime.
            stats_mode (int | str): set statistics mode (from 0 to 2)

                Allowed values:
                    * full: compute full frame histograms
                    * diff: compute histograms only for the part that differs from previous frame
                    * single: compute new histogram for each frame

                Defaults to full.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="palettegen",
            inputs=[self],
            named_arguments={
                "max_colors": max_colors,
                "reserve_transparent": reserve_transparent,
                "transparency_color": transparency_color,
                "stats_mode": stats_mode,
            },
        )[0]

    def paletteuse(
        self,
        palette_stream: "Stream",
        dither: Literal[
            "bayer",
            "heckbert",
            "floyd_steinberg",
            "sierra2",
            "sierra2_4a",
            "sierra3",
            "burkes",
            "atkinson",
        ]
        | int
        | None = None,
        bayer_scale: int | None = None,
        diff_mode: Literal["rectangle"] | int | None = None,
        new: bool | None = None,
        alpha_threshold: int | None = None,
        debug_kdtree: str | None = None,
    ) -> "Stream":
        """Use a palette to downsample an input video stream.

        Args:
            palette_stream (Stream): Input video stream.
            dither (int | str): select dithering mode (from 0 to 8)

                Allowed values:
                    * bayer: ordered 8x8 bayer dithering (deterministic)
                    * heckbert: dithering as defined by Paul Heckbert in 1982 (simple error diffusion)
                    * floyd_steinberg: Floyd and Steingberg dithering (error diffusion)
                    * sierra2: Frankie Sierra dithering v2 (error diffusion)
                    * sierra2_4a: Frankie Sierra dithering v2 "Lite" (error diffusion)
                    * sierra3: Frankie Sierra dithering v3 (error diffusion)
                    * burkes: Burkes dithering (error diffusion)
                    * atkinson: Atkinson dithering by Bill Atkinson at Apple Computer (error diffusion)

                Defaults to sierra2_4a.
            bayer_scale (int): set scale for bayer dithering (from 0 to 5)

                Defaults to 2.
            diff_mode (int | str): set frame difference mode (from 0 to 1)

                Allowed values:
                    * rectangle: process smallest different rectangle

                Defaults to 0.
            new (bool): take new palette for each output frame

                Defaults to false.
            alpha_threshold (int): set the alpha threshold for transparency (from 0 to 255)

                Defaults to 128.
            debug_kdtree (str): save Graphviz graph of the kdtree in specified file


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="paletteuse",
            inputs=[self, palette_stream],
            named_arguments={
                "dither": dither,
                "bayer_scale": bayer_scale,
                "diff_mode": diff_mode,
                "new": new,
                "alpha_threshold": alpha_threshold,
                "debug_kdtree": debug_kdtree,
            },
        )[0]

    def pan(self, args: str | None = None) -> "Stream":
        """Remix channels with coefficients (panning).

        Args:
            args (str): No description available.


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pan",
            inputs=[self],
            named_arguments={
                "args": args,
            },
        )[0]

    def perms(
        self,
        mode: Literal["none", "ro", "rw", "toggle", "random"] | int | None = None,
        seed: str | None = None,
    ) -> "Stream":
        """Set permissions for the output video frame.

        Args:
            mode (int | str): select permissions mode (from 0 to 4)

                Allowed values:
                    * none: do nothing
                    * ro: set all output frames read-only
                    * rw: set all output frames writable
                    * toggle: switch permissions
                    * random: set permissions randomly

                Defaults to none.
            seed (str): set the seed for the random mode (from -1 to UINT32_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="perms",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "seed": seed,
            },
        )[0]

    def perspective(
        self,
        x0: str | None = None,
        y0: str | None = None,
        x1: str | None = None,
        y1: str | None = None,
        x2: str | None = None,
        y2: str | None = None,
        x3: str | None = None,
        y3: str | None = None,
        interpolation: Literal["linear", "cubic"] | int | None = None,
        sense: Literal["source", "destination"] | int | None = None,
        eval: Literal["init", "frame"] | int | None = None,
    ) -> "Stream":
        """Correct the perspective of video.

        Args:
            x0 (str): set top left x coordinate

                Defaults to 0.
            y0 (str): set top left y coordinate

                Defaults to 0.
            x1 (str): set top right x coordinate

                Defaults to W.
            y1 (str): set top right y coordinate

                Defaults to 0.
            x2 (str): set bottom left x coordinate

                Defaults to 0.
            y2 (str): set bottom left y coordinate

                Defaults to H.
            x3 (str): set bottom right x coordinate

                Defaults to W.
            y3 (str): set bottom right y coordinate

                Defaults to H.
            interpolation (int | str): set interpolation (from 0 to 1)

                Allowed values:
                    * linear
                    * cubic

                Defaults to linear.
            sense (int | str): specify the sense of the coordinates (from 0 to 1)

                Allowed values:
                    * source: specify locations in source to send to corners in destination
                    * destination: specify locations in destination to send corners of source

                Defaults to source.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions per-frame

                Defaults to init.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="perspective",
            inputs=[self],
            named_arguments={
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "x3": x3,
                "y3": y3,
                "interpolation": interpolation,
                "sense": sense,
                "eval": eval,
            },
        )[0]

    def phase(
        self,
        mode: Literal["p", "t", "b", "T", "B", "u", "U", "a", "A"] | int | None = None,
    ) -> "Stream":
        """Phase shift fields.

        Args:
            mode (int | str): set phase mode (from 0 to 8)

                Allowed values:
                    * p: progressive
                    * t: top first
                    * b: bottom first
                    * T: top first analyze
                    * B: bottom first analyze
                    * u: analyze
                    * U: full analyze
                    * a: auto
                    * A: auto analyze

                Defaults to A.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="phase",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def photosensitivity(
        self,
        frames: int | None = None,
        f: int | None = None,
        threshold: float | None = None,
        t: float | None = None,
        skip: int | None = None,
        bypass: bool | None = None,
    ) -> "Stream":
        """Filter out photosensitive epilepsy seizure-inducing flashes.

        Args:
            frames (int): set how many frames to use (from 2 to 240)

                Defaults to 30.
            f (int): set how many frames to use (from 2 to 240)

                Defaults to 30.
            threshold (float): set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX)

                Defaults to 1.
            t (float): set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX)

                Defaults to 1.
            skip (int): set pixels to skip when sampling frames (from 1 to 1024)

                Defaults to 1.
            bypass (bool): leave frames unchanged

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="photosensitivity",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "f": f,
                "threshold": threshold,
                "t": t,
                "skip": skip,
                "bypass": bypass,
            },
        )[0]

    def pixdesctest(
        self,
    ) -> "Stream":
        """Test pixel format definitions.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pixdesctest", inputs=[self], named_arguments={}
        )[0]

    def pixelize(
        self,
        width: int | None = None,
        w: int | None = None,
        height: int | None = None,
        h: int | None = None,
        mode: Literal["avg", "min", "max"] | int | None = None,
        m: Literal["avg", "min", "max"] | int | None = None,
        planes: str | None = None,
        p: str | None = None,
    ) -> "Stream":
        """Pixelize video.

        Args:
            width (int): set block width (from 1 to 1024)

                Defaults to 16.
            w (int): set block width (from 1 to 1024)

                Defaults to 16.
            height (int): set block height (from 1 to 1024)

                Defaults to 16.
            h (int): set block height (from 1 to 1024)

                Defaults to 16.
            mode (int | str): set the pixelize mode (from 0 to 2)

                Allowed values:
                    * avg: average
                    * min: minimum
                    * max: maximum

                Defaults to avg.
            m (int | str): set the pixelize mode (from 0 to 2)

                Allowed values:
                    * avg: average
                    * min: minimum
                    * max: maximum

                Defaults to avg.
            planes (str): set what planes to filter

                Defaults to F.
            p (str): set what planes to filter

                Defaults to F.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pixelize",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "mode": mode,
                "m": m,
                "planes": planes,
                "p": p,
            },
        )[0]

    def pixscope(
        self,
        x: float | None = None,
        y: float | None = None,
        w: int | None = None,
        h: int | None = None,
        o: float | None = None,
        wx: float | None = None,
        wy: float | None = None,
    ) -> "Stream":
        """Pixel data analysis.

        Args:
            x (float): set scope x offset (from 0 to 1)

                Defaults to 0.5.
            y (float): set scope y offset (from 0 to 1)

                Defaults to 0.5.
            w (int): set scope width (from 1 to 80)

                Defaults to 7.
            h (int): set scope height (from 1 to 80)

                Defaults to 7.
            o (float): set window opacity (from 0 to 1)

                Defaults to 0.5.
            wx (float): set window x offset (from -1 to 1)

                Defaults to -1.
            wy (float): set window y offset (from -1 to 1)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pixscope",
            inputs=[self],
            named_arguments={
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "o": o,
                "wx": wx,
                "wy": wy,
            },
        )[0]

    def pp7(
        self,
        qp: int | None = None,
        mode: Literal["hard", "soft", "medium"] | int | None = None,
    ) -> "Stream":
        """Apply Postprocessing 7 filter.

        Args:
            qp (int): force a constant quantizer parameter (from 0 to 64)

                Defaults to 0.
            mode (int | str): set thresholding mode (from 0 to 2)

                Allowed values:
                    * hard: hard thresholding
                    * soft: soft thresholding
                    * medium: medium thresholding

                Defaults to medium.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pp7",
            inputs=[self],
            named_arguments={
                "qp": qp,
                "mode": mode,
            },
        )[0]

    def premultiply(
        self, *streams: "Stream", planes: int | None = None, inplace: bool | None = None
    ) -> "Stream":
        """PreMultiply first stream with first plane of second stream.

        Args:
            *streams (Stream): One or more input streams.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.
            inplace (bool): enable inplace mode

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="premultiply",
            inputs=[self, *streams],
            named_arguments={
                "planes": planes,
                "inplace": inplace,
            },
        )[0]

    def prewitt(
        self,
        planes: int | None = None,
        scale: float | None = None,
        delta: float | None = None,
    ) -> "Stream":
        """Apply prewitt operator.

        Args:
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            scale (float): set scale (from 0 to 65535)

                Defaults to 1.
            delta (float): set delta (from -65535 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="prewitt",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def pseudocolor(
        self,
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
        index: int | None = None,
        i: int | None = None,
        preset: Literal[
            "none",
            "magma",
            "inferno",
            "plasma",
            "viridis",
            "turbo",
            "cividis",
            "range1",
            "range2",
            "shadows",
            "highlights",
            "solar",
            "nominal",
            "preferred",
            "total",
            "spectral",
            "cool",
            "heat",
            "fiery",
            "blues",
            "green",
            "helix",
        ]
        | int
        | None = None,
        p: Literal[
            "none",
            "magma",
            "inferno",
            "plasma",
            "viridis",
            "turbo",
            "cividis",
            "range1",
            "range2",
            "shadows",
            "highlights",
            "solar",
            "nominal",
            "preferred",
            "total",
            "spectral",
            "cool",
            "heat",
            "fiery",
            "blues",
            "green",
            "helix",
        ]
        | int
        | None = None,
        opacity: float | None = None,
    ) -> "Stream":
        """Make pseudocolored video frames.

        Args:
            c0 (str): set component #0 expression

                Defaults to val.
            c1 (str): set component #1 expression

                Defaults to val.
            c2 (str): set component #2 expression

                Defaults to val.
            c3 (str): set component #3 expression

                Defaults to val.
            index (int): set component as base (from 0 to 3)

                Defaults to 0.
            i (int): set component as base (from 0 to 3)

                Defaults to 0.
            preset (int | str): set preset (from -1 to 20)

                Allowed values:
                    * none
                    * magma
                    * inferno
                    * plasma
                    * viridis
                    * turbo
                    * cividis
                    * range1
                    * range2
                    * shadows
                    * highlights
                    * solar
                    * nominal
                    * preferred
                    * total
                    * spectral
                    * cool
                    * heat
                    * fiery
                    * blues
                    * green
                    * helix

                Defaults to none.
            p (int | str): set preset (from -1 to 20)

                Allowed values:
                    * none
                    * magma
                    * inferno
                    * plasma
                    * viridis
                    * turbo
                    * cividis
                    * range1
                    * range2
                    * shadows
                    * highlights
                    * solar
                    * nominal
                    * preferred
                    * total
                    * spectral
                    * cool
                    * heat
                    * fiery
                    * blues
                    * green
                    * helix

                Defaults to none.
            opacity (float): set pseudocolor opacity (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pseudocolor",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
                "index": index,
                "i": i,
                "preset": preset,
                "p": p,
                "opacity": opacity,
            },
        )[0]

    def psnr(
        self,
        reference_stream: "Stream",
        stats_file: str | None = None,
        f: str | None = None,
        stats_version: int | None = None,
        output_max: bool | None = None,
    ) -> "Stream":
        """Calculate the PSNR between two video streams.

        Args:
            reference_stream (Stream): Input video stream.
            stats_file (str): Set file where to store per-frame difference information

            f (str): Set file where to store per-frame difference information

            stats_version (int): Set the format version for the stats file. (from 1 to 2)

                Defaults to 1.
            output_max (bool): Add raw stats (max values) to the output log.

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="psnr",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
                "stats_version": stats_version,
                "output_max": output_max,
            },
        )[0]

    def pullup(
        self,
        jl: int | None = None,
        jr: int | None = None,
        jt: int | None = None,
        jb: int | None = None,
        sb: bool | None = None,
        mp: Literal["y", "u", "v"] | int | None = None,
    ) -> "Stream":
        """Pullup from field sequence to frames.

        Args:
            jl (int): set left junk size (from 0 to INT_MAX)

                Defaults to 1.
            jr (int): set right junk size (from 0 to INT_MAX)

                Defaults to 1.
            jt (int): set top junk size (from 1 to INT_MAX)

                Defaults to 4.
            jb (int): set bottom junk size (from 1 to INT_MAX)

                Defaults to 4.
            sb (bool): set strict breaks

                Defaults to false.
            mp (int | str): set metric plane (from 0 to 2)

                Allowed values:
                    * y: luma
                    * u: chroma blue
                    * v: chroma red

                Defaults to y.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="pullup",
            inputs=[self],
            named_arguments={
                "jl": jl,
                "jr": jr,
                "jt": jt,
                "jb": jb,
                "sb": sb,
                "mp": mp,
            },
        )[0]

    def qp(self, qp: str | None = None) -> "Stream":
        """Change video quantization parameters.

        Args:
            qp (str): set qp expression


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="qp",
            inputs=[self],
            named_arguments={
                "qp": qp,
            },
        )[0]

    def random(self, frames: int | None = None, seed: str | None = None) -> "Stream":
        """Return random frames.

        Args:
            frames (int): set number of frames in cache (from 2 to 512)

                Defaults to 30.
            seed (str): set the seed (from -1 to UINT32_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="random",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "seed": seed,
            },
        )[0]

    def readeia608(
        self,
        scan_min: int | None = None,
        scan_max: int | None = None,
        spw: float | None = None,
        chp: bool | None = None,
        lp: bool | None = None,
    ) -> "Stream":
        """Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

        Args:
            scan_min (int): set from which line to scan for codes (from 0 to INT_MAX)

                Defaults to 0.
            scan_max (int): set to which line to scan for codes (from 0 to INT_MAX)

                Defaults to 29.
            spw (float): set ratio of width reserved for sync code detection (from 0.1 to 0.7)

                Defaults to 0.27.
            chp (bool): check and apply parity bit

                Defaults to false.
            lp (bool): lowpass line prior to processing

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="readeia608",
            inputs=[self],
            named_arguments={
                "scan_min": scan_min,
                "scan_max": scan_max,
                "spw": spw,
                "chp": chp,
                "lp": lp,
            },
        )[0]

    def readvitc(
        self,
        scan_max: int | None = None,
        thr_b: float | None = None,
        thr_w: float | None = None,
    ) -> "Stream":
        """Read vertical interval timecode and write it to frame metadata.

        Args:
            scan_max (int): maximum line numbers to scan for VITC data (from -1 to INT_MAX)

                Defaults to 45.
            thr_b (float): black color threshold (from 0 to 1)

                Defaults to 0.2.
            thr_w (float): white color threshold (from 0 to 1)

                Defaults to 0.6.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="readvitc",
            inputs=[self],
            named_arguments={
                "scan_max": scan_max,
                "thr_b": thr_b,
                "thr_w": thr_w,
            },
        )[0]

    def realtime(
        self, limit: str | None = None, speed: float | None = None
    ) -> "Stream":
        """Slow down filtering to match realtime.

        Args:
            limit (str): sleep time limit

                Defaults to 2.
            speed (float): speed factor (from DBL_MIN to DBL_MAX)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="realtime",
            inputs=[self],
            named_arguments={
                "limit": limit,
                "speed": speed,
            },
        )[0]

    def remap(
        self,
        xmap_stream: "Stream",
        ymap_stream: "Stream",
        format: Literal["color", "gray"] | int | None = None,
        fill: str | None = None,
    ) -> "Stream":
        """Remap pixels.

        Args:
            xmap_stream (Stream): Input video stream.
            ymap_stream (Stream): Input video stream.
            format (int | str): set output format (from 0 to 1)

                Allowed values:
                    * color
                    * gray

                Defaults to color.
            fill (str): set the color of the unmapped pixels

                Defaults to black.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="remap",
            inputs=[self, xmap_stream, ymap_stream],
            named_arguments={
                "format": format,
                "fill": fill,
            },
        )[0]

    def removegrain(
        self,
        m0: int | None = None,
        m1: int | None = None,
        m2: int | None = None,
        m3: int | None = None,
    ) -> "Stream":
        """Remove grain.

        Args:
            m0 (int): set mode for 1st plane (from 0 to 24)

                Defaults to 0.
            m1 (int): set mode for 2nd plane (from 0 to 24)

                Defaults to 0.
            m2 (int): set mode for 3rd plane (from 0 to 24)

                Defaults to 0.
            m3 (int): set mode for 4th plane (from 0 to 24)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="removegrain",
            inputs=[self],
            named_arguments={
                "m0": m0,
                "m1": m1,
                "m2": m2,
                "m3": m3,
            },
        )[0]

    def removelogo(self, filename: str | None = None, f: str | None = None) -> "Stream":
        """Remove a TV logo based on a mask image.

        Args:
            filename (str): set bitmap filename

            f (str): set bitmap filename


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="removelogo",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
            },
        )[0]

    def repeatfields(
        self,
    ) -> "Stream":
        """Hard repeat fields based on MPEG repeat field flag.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="repeatfields", inputs=[self], named_arguments={}
        )[0]

    def replaygain(
        self, track_gain: float | None = None, track_peak: float | None = None
    ) -> "Stream":
        """ReplayGain scanner.

        Args:
            track_gain (float): track gain (dB) (from -FLT_MAX to FLT_MAX)

                Defaults to 0.
            track_peak (float): track peak (from -FLT_MAX to FLT_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="replaygain",
            inputs=[self],
            named_arguments={
                "track_gain": track_gain,
                "track_peak": track_peak,
            },
        )[0]

    def reverse(
        self,
    ) -> "Stream":
        """Reverse a clip.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="reverse", inputs=[self], named_arguments={}
        )[0]

    def rgbashift(
        self,
        rh: int | None = None,
        rv: int | None = None,
        gh: int | None = None,
        gv: int | None = None,
        bh: int | None = None,
        bv: int | None = None,
        ah: int | None = None,
        av: int | None = None,
        edge: Literal["smear", "wrap"] | int | None = None,
    ) -> "Stream":
        """Shift RGBA.

        Args:
            rh (int): shift red horizontally (from -255 to 255)

                Defaults to 0.
            rv (int): shift red vertically (from -255 to 255)

                Defaults to 0.
            gh (int): shift green horizontally (from -255 to 255)

                Defaults to 0.
            gv (int): shift green vertically (from -255 to 255)

                Defaults to 0.
            bh (int): shift blue horizontally (from -255 to 255)

                Defaults to 0.
            bv (int): shift blue vertically (from -255 to 255)

                Defaults to 0.
            ah (int): shift alpha horizontally (from -255 to 255)

                Defaults to 0.
            av (int): shift alpha vertically (from -255 to 255)

                Defaults to 0.
            edge (int | str): set edge operation (from 0 to 1)

                Allowed values:
                    * smear
                    * wrap

                Defaults to smear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="rgbashift",
            inputs=[self],
            named_arguments={
                "rh": rh,
                "rv": rv,
                "gh": gh,
                "gv": gv,
                "bh": bh,
                "bv": bv,
                "ah": ah,
                "av": av,
                "edge": edge,
            },
        )[0]

    def roberts(
        self,
        planes: int | None = None,
        scale: float | None = None,
        delta: float | None = None,
    ) -> "Stream":
        """Apply roberts cross operator.

        Args:
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            scale (float): set scale (from 0 to 65535)

                Defaults to 1.
            delta (float): set delta (from -65535 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="roberts",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def rotate(
        self,
        angle: str | None = None,
        a: str | None = None,
        out_w: str | None = None,
        ow: str | None = None,
        out_h: str | None = None,
        oh: str | None = None,
        fillcolor: str | None = None,
        c: str | None = None,
        bilinear: bool | None = None,
    ) -> "Stream":
        """Rotate the input image.

        Args:
            angle (str): set angle (in radians)

                Defaults to 0.
            a (str): set angle (in radians)

                Defaults to 0.
            out_w (str): set output width expression

                Defaults to iw.
            ow (str): set output width expression

                Defaults to iw.
            out_h (str): set output height expression

                Defaults to ih.
            oh (str): set output height expression

                Defaults to ih.
            fillcolor (str): set background fill color

                Defaults to black.
            c (str): set background fill color

                Defaults to black.
            bilinear (bool): use bilinear interpolation

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="rotate",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "a": a,
                "out_w": out_w,
                "ow": ow,
                "out_h": out_h,
                "oh": oh,
                "fillcolor": fillcolor,
                "c": c,
                "bilinear": bilinear,
            },
        )[0]

    def rubberband(
        self,
        tempo: float | None = None,
        pitch: float | None = None,
        transients: Literal["crisp", "mixed", "smooth"] | int | None = None,
        detector: Literal["compound", "percussive", "soft"] | int | None = None,
        phase: Literal["laminar", "independent"] | int | None = None,
        window: Literal["standard", "short", "long"] | int | None = None,
        smoothing: Literal["off", "on"] | int | None = None,
        formant: Literal["shifted", "preserved"] | int | None = None,
        pitchq: Literal["quality", "speed", "consistency"] | int | None = None,
        channels: Literal["apart", "together"] | int | None = None,
    ) -> "Stream":
        """Apply time-stretching and pitch-shifting.

        Args:
            tempo (float): set tempo scale factor (from 0.01 to 100)

                Defaults to 1.
            pitch (float): set pitch scale factor (from 0.01 to 100)

                Defaults to 1.
            transients (int | str): set transients (from 0 to INT_MAX)

                Allowed values:
                    * crisp
                    * mixed
                    * smooth

                Defaults to crisp.
            detector (int | str): set detector (from 0 to INT_MAX)

                Allowed values:
                    * compound
                    * percussive
                    * soft

                Defaults to compound.
            phase (int | str): set phase (from 0 to INT_MAX)

                Allowed values:
                    * laminar
                    * independent

                Defaults to laminar.
            window (int | str): set window (from 0 to INT_MAX)

                Allowed values:
                    * standard
                    * short
                    * long

                Defaults to standard.
            smoothing (int | str): set smoothing (from 0 to INT_MAX)

                Allowed values:
                    * off
                    * on

                Defaults to off.
            formant (int | str): set formant (from 0 to INT_MAX)

                Allowed values:
                    * shifted
                    * preserved

                Defaults to shifted.
            pitchq (int | str): set pitch quality (from 0 to INT_MAX)

                Allowed values:
                    * quality
                    * speed
                    * consistency

                Defaults to speed.
            channels (int | str): set channels (from 0 to INT_MAX)

                Allowed values:
                    * apart
                    * together

                Defaults to apart.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="rubberband",
            inputs=[self],
            named_arguments={
                "tempo": tempo,
                "pitch": pitch,
                "transients": transients,
                "detector": detector,
                "phase": phase,
                "window": window,
                "smoothing": smoothing,
                "formant": formant,
                "pitchq": pitchq,
                "channels": channels,
            },
        )[0]

    def sab(
        self,
        luma_radius: float | None = None,
        lr: float | None = None,
        luma_pre_filter_radius: float | None = None,
        lpfr: float | None = None,
        luma_strength: float | None = None,
        ls: float | None = None,
        chroma_radius: float | None = None,
        cr: float | None = None,
        chroma_pre_filter_radius: float | None = None,
        cpfr: float | None = None,
        chroma_strength: float | None = None,
        cs: float | None = None,
    ) -> "Stream":
        """Apply shape adaptive blur.

        Args:
            luma_radius (float): set luma radius (from 0.1 to 4)

                Defaults to 1.
            lr (float): set luma radius (from 0.1 to 4)

                Defaults to 1.
            luma_pre_filter_radius (float): set luma pre-filter radius (from 0.1 to 2)

                Defaults to 1.
            lpfr (float): set luma pre-filter radius (from 0.1 to 2)

                Defaults to 1.
            luma_strength (float): set luma strength (from 0.1 to 100)

                Defaults to 1.
            ls (float): set luma strength (from 0.1 to 100)

                Defaults to 1.
            chroma_radius (float): set chroma radius (from -0.9 to 4)

                Defaults to -0.9.
            cr (float): set chroma radius (from -0.9 to 4)

                Defaults to -0.9.
            chroma_pre_filter_radius (float): set chroma pre-filter radius (from -0.9 to 2)

                Defaults to -0.9.
            cpfr (float): set chroma pre-filter radius (from -0.9 to 2)

                Defaults to -0.9.
            chroma_strength (float): set chroma strength (from -0.9 to 100)

                Defaults to -0.9.
            cs (float): set chroma strength (from -0.9 to 100)

                Defaults to -0.9.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sab",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_pre_filter_radius": luma_pre_filter_radius,
                "lpfr": lpfr,
                "luma_strength": luma_strength,
                "ls": ls,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_pre_filter_radius": chroma_pre_filter_radius,
                "cpfr": cpfr,
                "chroma_strength": chroma_strength,
                "cs": cs,
            },
        )[0]

    def scale(
        self,
        w: str | None = None,
        width: str | None = None,
        h: str | None = None,
        height: str | None = None,
        flags: str | None = None,
        interl: bool | None = None,
        size: str | None = None,
        s: str | None = None,
        in_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int
        | None = None,
        out_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int
        | None = None,
        in_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int
        | None = None,
        out_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int
        | None = None,
        in_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int
        | None = None,
        out_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int
        | None = None,
        in_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        out_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        in_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int
        | None = None,
        out_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int
        | None = None,
        in_v_chr_pos: int | None = None,
        in_h_chr_pos: int | None = None,
        out_v_chr_pos: int | None = None,
        out_h_chr_pos: int | None = None,
        force_original_aspect_ratio: Literal["disable", "decrease", "increase"]
        | int
        | None = None,
        force_divisible_by: int | None = None,
        reset_sar: bool | None = None,
        param0: float | None = None,
        param1: float | None = None,
        eval: Literal["init", "frame"] | int | None = None,
    ) -> "Stream":
        """Scale the input video size and/or convert the image format.

        Args:
            w (str): Output video width

            width (str): Output video width

            h (str): Output video height

            height (str): Output video height

            flags (str): Flags to pass to libswscale

            interl (bool): set interlacing

                Defaults to false.
            size (str): set video size

            s (str): set video size

            in_color_matrix (int | str): set input YCbCr type (from -1 to 17)

                Allowed values:
                    * auto
                    * bt601
                    * bt470
                    * smpte170m
                    * bt709
                    * fcc
                    * smpte240m
                    * bt2020

                Defaults to auto.
            out_color_matrix (int | str): set output YCbCr type (from 0 to 17)

                Allowed values:
                    * auto
                    * bt601
                    * bt470
                    * smpte170m
                    * bt709
                    * fcc
                    * smpte240m
                    * bt2020

                Defaults to 2.
            in_range (int | str): set input color range (from 0 to 2)

                Allowed values:
                    * auto
                    * unknown
                    * full
                    * limited
                    * jpeg
                    * mpeg
                    * tv
                    * pc

                Defaults to auto.
            out_range (int | str): set output color range (from 0 to 2)

                Allowed values:
                    * auto
                    * unknown
                    * full
                    * limited
                    * jpeg
                    * mpeg
                    * tv
                    * pc

                Defaults to auto.
            in_chroma_loc (int | str): set input chroma sample location (from 0 to 6)

                Allowed values:
                    * auto
                    * unknown
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to auto.
            out_chroma_loc (int | str): set output chroma sample location (from 0 to 6)

                Allowed values:
                    * auto
                    * unknown
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to auto.
            in_primaries (int | str): set input primaries (from -1 to 22)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to auto.
            out_primaries (int | str): set output primaries (from -1 to 22)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to auto.
            in_transfer (int | str): set output color transfer (from -1 to 18)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * iec61966-2-1
                    * srgb
                    * iec61966-2-4
                    * xvycc
                    * bt1361e
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * smpte428
                    * arib-std-b67

                Defaults to auto.
            out_transfer (int | str): set output color transfer (from -1 to 18)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * iec61966-2-1
                    * srgb
                    * iec61966-2-4
                    * xvycc
                    * bt1361e
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * smpte428
                    * arib-std-b67

                Defaults to auto.
            in_v_chr_pos (int): input vertical chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            in_h_chr_pos (int): input horizontal chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            out_v_chr_pos (int): output vertical chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            out_h_chr_pos (int): output horizontal chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            force_original_aspect_ratio (int | str): decrease or increase w/h if necessary to keep the original AR (from 0 to 2)

                Allowed values:
                    * disable
                    * decrease
                    * increase

                Defaults to disable.
            force_divisible_by (int): enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256)

                Defaults to 1.
            reset_sar (bool): reset SAR to 1 and scale to square pixels if scaling proportionally

                Defaults to false.
            param0 (float): Scaler param 0 (from -DBL_MAX to DBL_MAX)

                Defaults to DBL_MAX.
            param1 (float): Scaler param 1 (from -DBL_MAX to DBL_MAX)

                Defaults to DBL_MAX.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions during initialization and per-frame

                Defaults to init.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="scale",
            inputs=[self],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "flags": flags,
                "interl": interl,
                "size": size,
                "s": s,
                "in_color_matrix": in_color_matrix,
                "out_color_matrix": out_color_matrix,
                "in_range": in_range,
                "out_range": out_range,
                "in_chroma_loc": in_chroma_loc,
                "out_chroma_loc": out_chroma_loc,
                "in_primaries": in_primaries,
                "out_primaries": out_primaries,
                "in_transfer": in_transfer,
                "out_transfer": out_transfer,
                "in_v_chr_pos": in_v_chr_pos,
                "in_h_chr_pos": in_h_chr_pos,
                "out_v_chr_pos": out_v_chr_pos,
                "out_h_chr_pos": out_h_chr_pos,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                "reset_sar": reset_sar,
                "param0": param0,
                "param1": param1,
                "eval": eval,
            },
        )[0]

    def scale2ref(
        self,
        ref_stream: "Stream",
        w: str | None = None,
        width: str | None = None,
        h: str | None = None,
        height: str | None = None,
        flags: str | None = None,
        interl: bool | None = None,
        size: str | None = None,
        s: str | None = None,
        in_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int
        | None = None,
        out_color_matrix: Literal[
            "auto", "bt601", "bt470", "smpte170m", "bt709", "fcc", "smpte240m", "bt2020"
        ]
        | int
        | None = None,
        in_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int
        | None = None,
        out_range: Literal[
            "auto", "unknown", "full", "limited", "jpeg", "mpeg", "tv", "pc"
        ]
        | int
        | None = None,
        in_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int
        | None = None,
        out_chroma_loc: Literal[
            "auto",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int
        | None = None,
        in_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        out_primaries: Literal[
            "auto",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        in_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int
        | None = None,
        out_transfer: Literal[
            "auto",
            "bt709",
            "bt470m",
            "gamma22",
            "bt470bg",
            "gamma28",
            "smpte170m",
            "smpte240m",
            "linear",
            "iec61966-2-1",
            "srgb",
            "iec61966-2-4",
            "xvycc",
            "bt1361e",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int
        | None = None,
        in_v_chr_pos: int | None = None,
        in_h_chr_pos: int | None = None,
        out_v_chr_pos: int | None = None,
        out_h_chr_pos: int | None = None,
        force_original_aspect_ratio: Literal["disable", "decrease", "increase"]
        | int
        | None = None,
        force_divisible_by: int | None = None,
        reset_sar: bool | None = None,
        param0: float | None = None,
        param1: float | None = None,
        eval: Literal["init", "frame"] | int | None = None,
    ) -> list["Stream"]:
        """Scale the input video size and/or convert the image format to the given reference.

        Args:
            ref_stream (Stream): Input video stream.
            w (str): Output video width

            width (str): Output video width

            h (str): Output video height

            height (str): Output video height

            flags (str): Flags to pass to libswscale

            interl (bool): set interlacing

                Defaults to false.
            size (str): set video size

            s (str): set video size

            in_color_matrix (int | str): set input YCbCr type (from -1 to 17)

                Allowed values:
                    * auto
                    * bt601
                    * bt470
                    * smpte170m
                    * bt709
                    * fcc
                    * smpte240m
                    * bt2020

                Defaults to auto.
            out_color_matrix (int | str): set output YCbCr type (from 0 to 17)

                Allowed values:
                    * auto
                    * bt601
                    * bt470
                    * smpte170m
                    * bt709
                    * fcc
                    * smpte240m
                    * bt2020

                Defaults to 2.
            in_range (int | str): set input color range (from 0 to 2)

                Allowed values:
                    * auto
                    * unknown
                    * full
                    * limited
                    * jpeg
                    * mpeg
                    * tv
                    * pc

                Defaults to auto.
            out_range (int | str): set output color range (from 0 to 2)

                Allowed values:
                    * auto
                    * unknown
                    * full
                    * limited
                    * jpeg
                    * mpeg
                    * tv
                    * pc

                Defaults to auto.
            in_chroma_loc (int | str): set input chroma sample location (from 0 to 6)

                Allowed values:
                    * auto
                    * unknown
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to auto.
            out_chroma_loc (int | str): set output chroma sample location (from 0 to 6)

                Allowed values:
                    * auto
                    * unknown
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to auto.
            in_primaries (int | str): set input primaries (from -1 to 22)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to auto.
            out_primaries (int | str): set output primaries (from -1 to 22)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to auto.
            in_transfer (int | str): set output color transfer (from -1 to 18)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * iec61966-2-1
                    * srgb
                    * iec61966-2-4
                    * xvycc
                    * bt1361e
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * smpte428
                    * arib-std-b67

                Defaults to auto.
            out_transfer (int | str): set output color transfer (from -1 to 18)

                Allowed values:
                    * auto
                    * bt709
                    * bt470m
                    * gamma22
                    * bt470bg
                    * gamma28
                    * smpte170m
                    * smpte240m
                    * linear
                    * iec61966-2-1
                    * srgb
                    * iec61966-2-4
                    * xvycc
                    * bt1361e
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * smpte428
                    * arib-std-b67

                Defaults to auto.
            in_v_chr_pos (int): input vertical chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            in_h_chr_pos (int): input horizontal chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            out_v_chr_pos (int): output vertical chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            out_h_chr_pos (int): output horizontal chroma position in luma grid/256 (from -513 to 512)

                Defaults to -513.
            force_original_aspect_ratio (int | str): decrease or increase w/h if necessary to keep the original AR (from 0 to 2)

                Allowed values:
                    * disable
                    * decrease
                    * increase

                Defaults to disable.
            force_divisible_by (int): enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256)

                Defaults to 1.
            reset_sar (bool): reset SAR to 1 and scale to square pixels if scaling proportionally

                Defaults to false.
            param0 (float): Scaler param 0 (from -DBL_MAX to DBL_MAX)

                Defaults to DBL_MAX.
            param1 (float): Scaler param 1 (from -DBL_MAX to DBL_MAX)

                Defaults to DBL_MAX.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions during initialization and per-frame

                Defaults to init.

        Returns:
            list["Stream"]: A list of 2 Stream objects.
        """
        return self._apply_filter(
            filter_name="scale2ref",
            inputs=[self, ref_stream],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "flags": flags,
                "interl": interl,
                "size": size,
                "s": s,
                "in_color_matrix": in_color_matrix,
                "out_color_matrix": out_color_matrix,
                "in_range": in_range,
                "out_range": out_range,
                "in_chroma_loc": in_chroma_loc,
                "out_chroma_loc": out_chroma_loc,
                "in_primaries": in_primaries,
                "out_primaries": out_primaries,
                "in_transfer": in_transfer,
                "out_transfer": out_transfer,
                "in_v_chr_pos": in_v_chr_pos,
                "in_h_chr_pos": in_h_chr_pos,
                "out_v_chr_pos": out_v_chr_pos,
                "out_h_chr_pos": out_h_chr_pos,
                "force_original_aspect_ratio": force_original_aspect_ratio,
                "force_divisible_by": force_divisible_by,
                "reset_sar": reset_sar,
                "param0": param0,
                "param1": param1,
                "eval": eval,
            },
            num_output_streams=2,
        )

    def scale_vt(
        self,
        w: str | None = None,
        h: str | None = None,
        color_matrix: str | None = None,
        color_primaries: str | None = None,
        color_transfer: str | None = None,
    ) -> "Stream":
        """Scale Videotoolbox frames

        Args:
            w (str): Output video width

                Defaults to iw.
            h (str): Output video height

                Defaults to ih.
            color_matrix (str): Output colour matrix coefficient set

            color_primaries (str): Output colour primaries

            color_transfer (str): Output colour transfer characteristics


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="scale_vt",
            inputs=[self],
            named_arguments={
                "w": w,
                "h": h,
                "color_matrix": color_matrix,
                "color_primaries": color_primaries,
                "color_transfer": color_transfer,
            },
        )[0]

    def scdet(
        self,
        threshold: float | None = None,
        t: float | None = None,
        sc_pass: bool | None = None,
        s: bool | None = None,
    ) -> "Stream":
        """Detect video scene change

        Args:
            threshold (float): set scene change detect threshold (from 0 to 100)

                Defaults to 10.
            t (float): set scene change detect threshold (from 0 to 100)

                Defaults to 10.
            sc_pass (bool): Set the flag to pass scene change frames

                Defaults to false.
            s (bool): Set the flag to pass scene change frames

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="scdet",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "t": t,
                "sc_pass": sc_pass,
                "s": s,
            },
        )[0]

    def scharr(
        self,
        planes: int | None = None,
        scale: float | None = None,
        delta: float | None = None,
    ) -> "Stream":
        """Apply scharr operator.

        Args:
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            scale (float): set scale (from 0 to 65535)

                Defaults to 1.
            delta (float): set delta (from -65535 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="scharr",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def scroll(
        self,
        horizontal: float | None = None,
        h: float | None = None,
        vertical: float | None = None,
        v: float | None = None,
        hpos: float | None = None,
        vpos: float | None = None,
    ) -> "Stream":
        """Scroll input video.

        Args:
            horizontal (float): set the horizontal scrolling speed (from -1 to 1)

                Defaults to 0.
            h (float): set the horizontal scrolling speed (from -1 to 1)

                Defaults to 0.
            vertical (float): set the vertical scrolling speed (from -1 to 1)

                Defaults to 0.
            v (float): set the vertical scrolling speed (from -1 to 1)

                Defaults to 0.
            hpos (float): set initial horizontal position (from 0 to 1)

                Defaults to 0.
            vpos (float): set initial vertical position (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="scroll",
            inputs=[self],
            named_arguments={
                "horizontal": horizontal,
                "h": h,
                "vertical": vertical,
                "v": v,
                "hpos": hpos,
                "vpos": vpos,
            },
        )[0]

    def segment(
        self, timestamps: str | None = None, frames: str | None = None
    ) -> "FilterMultiOutput":
        """Segment video stream.

        Args:
            timestamps (str): timestamps of input at which to split input

            frames (str): frames at which to split input


        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="segment",
            inputs=[self],
            named_arguments={
                "timestamps": timestamps,
                "frames": frames,
            },
        )

    def select(
        self,
        expr: str | None = None,
        e: str | None = None,
        outputs: int | None = None,
        n: int | None = None,
    ) -> "FilterMultiOutput":
        """Select video frames to pass in output.

        Args:
            expr (str): set an expression to use for selecting frames

                Defaults to 1.
            e (str): set an expression to use for selecting frames

                Defaults to 1.
            outputs (int): set the number of outputs (from 1 to INT_MAX)

                Defaults to 1.
            n (int): set the number of outputs (from 1 to INT_MAX)

                Defaults to 1.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="select",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "e": e,
                "outputs": outputs,
                "n": n,
            },
        )

    def selectivecolor(
        self,
        correction_method: Literal["absolute", "relative"] | int | None = None,
        reds: str | None = None,
        yellows: str | None = None,
        greens: str | None = None,
        cyans: str | None = None,
        blues: str | None = None,
        magentas: str | None = None,
        whites: str | None = None,
        neutrals: str | None = None,
        blacks: str | None = None,
        psfile: str | None = None,
    ) -> "Stream":
        """Apply CMYK adjustments to specific color ranges.

        Args:
            correction_method (int | str): select correction method (from 0 to 1)

                Allowed values:
                    * absolute
                    * relative

                Defaults to absolute.
            reds (str): adjust red regions

            yellows (str): adjust yellow regions

            greens (str): adjust green regions

            cyans (str): adjust cyan regions

            blues (str): adjust blue regions

            magentas (str): adjust magenta regions

            whites (str): adjust white regions

            neutrals (str): adjust neutral regions

            blacks (str): adjust black regions

            psfile (str): set Photoshop selectivecolor file name


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="selectivecolor",
            inputs=[self],
            named_arguments={
                "correction_method": correction_method,
                "reds": reds,
                "yellows": yellows,
                "greens": greens,
                "cyans": cyans,
                "blues": blues,
                "magentas": magentas,
                "whites": whites,
                "neutrals": neutrals,
                "blacks": blacks,
                "psfile": psfile,
            },
        )[0]

    def sendcmd(
        self,
        commands: str | None = None,
        c: str | None = None,
        filename: str | None = None,
        f: str | None = None,
    ) -> "Stream":
        """Send commands to filters.

        Args:
            commands (str): set commands

            c (str): set commands

            filename (str): set commands file

            f (str): set commands file


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sendcmd",
            inputs=[self],
            named_arguments={
                "commands": commands,
                "c": c,
                "filename": filename,
                "f": f,
            },
        )[0]

    def separatefields(
        self,
    ) -> "Stream":
        """Split input video frames into fields.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="separatefields", inputs=[self], named_arguments={}
        )[0]

    def setdar(
        self,
        dar: str | None = None,
        ratio: str | None = None,
        r: str | None = None,
        max: int | None = None,
    ) -> "Stream":
        """Set the frame display aspect ratio.

        Args:
            dar (str): set display aspect ratio

                Defaults to 0.
            ratio (str): set display aspect ratio

                Defaults to 0.
            r (str): set display aspect ratio

                Defaults to 0.
            max (int): set max value for nominator or denominator in the ratio (from 1 to INT_MAX)

                Defaults to 100.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setdar",
            inputs=[self],
            named_arguments={
                "dar": dar,
                "ratio": ratio,
                "r": r,
                "max": max,
            },
        )[0]

    def setfield(
        self, mode: Literal["auto", "bff", "tff", "prog"] | int | None = None
    ) -> "Stream":
        """Force field for the output video frame.

        Args:
            mode (int | str): select interlace mode (from -1 to 2)

                Allowed values:
                    * auto: keep the same input field
                    * bff: mark as bottom-field-first
                    * tff: mark as top-field-first
                    * prog: mark as progressive

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setfield",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def setparams(
        self,
        field_mode: Literal["auto", "bff", "tff", "prog"] | int | None = None,
        range: Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
        | int
        | None = None,
        color_primaries: Literal[
            "auto",
            "bt709",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        color_trc: Literal[
            "auto",
            "bt709",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "linear",
            "log100",
            "log316",
            "iec61966-2-4",
            "bt1361e",
            "iec61966-2-1",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "smpte428",
            "arib-std-b67",
        ]
        | int
        | None = None,
        colorspace: Literal[
            "auto",
            "gbr",
            "bt709",
            "unknown",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "ycgco-re",
            "ycgco-ro",
            "bt2020nc",
            "bt2020c",
            "smpte2085",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
            "ipt-c2",
        ]
        | int
        | None = None,
        chroma_location: Literal[
            "auto",
            "unspecified",
            "unknown",
            "left",
            "center",
            "topleft",
            "top",
            "bottomleft",
            "bottom",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Force field, or color property for the output video frame.

        Args:
            field_mode (int | str): select interlace mode (from -1 to 2)

                Allowed values:
                    * auto: keep the same input field
                    * bff: mark as bottom-field-first
                    * tff: mark as top-field-first
                    * prog: mark as progressive

                Defaults to auto.
            range (int | str): select color range (from -1 to 2)

                Allowed values:
                    * auto: keep the same color range
                    * unspecified
                    * unknown
                    * limited
                    * tv
                    * mpeg
                    * full
                    * pc
                    * jpeg

                Defaults to auto.
            color_primaries (int | str): select color primaries (from -1 to 22)

                Allowed values:
                    * auto: keep the same color primaries
                    * bt709
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to auto.
            color_trc (int | str): select color transfer (from -1 to 18)

                Allowed values:
                    * auto: keep the same color transfer
                    * bt709
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * linear
                    * log100
                    * log316
                    * iec61966-2-4
                    * bt1361e
                    * iec61966-2-1
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * smpte428
                    * arib-std-b67

                Defaults to auto.
            colorspace (int | str): select colorspace (from -1 to 17)

                Allowed values:
                    * auto: keep the same colorspace
                    * gbr
                    * bt709
                    * unknown
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * ycgco-re
                    * ycgco-ro
                    * bt2020nc
                    * bt2020c
                    * smpte2085
                    * chroma-derived-nc
                    * chroma-derived-c
                    * ictcp
                    * ipt-c2

                Defaults to auto.
            chroma_location (int | str): select chroma sample location (from -1 to 6)

                Allowed values:
                    * auto: keep the same chroma location
                    * unspecified
                    * unknown
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setparams",
            inputs=[self],
            named_arguments={
                "field_mode": field_mode,
                "range": range,
                "color_primaries": color_primaries,
                "color_trc": color_trc,
                "colorspace": colorspace,
                "chroma_location": chroma_location,
            },
        )[0]

    def setpts(
        self, expr: str | None = None, strip_fps: bool | None = None
    ) -> "Stream":
        """Set PTS for the output video frame.

        Args:
            expr (str): Expression determining the frame timestamp

                Defaults to PTS.
            strip_fps (bool): Unset framerate metadata

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setpts",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "strip_fps": strip_fps,
            },
        )[0]

    def setrange(
        self,
        range: Literal[
            "auto",
            "unspecified",
            "unknown",
            "limited",
            "tv",
            "mpeg",
            "full",
            "pc",
            "jpeg",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Force color range for the output video frame.

        Args:
            range (int | str): select color range (from -1 to 2)

                Allowed values:
                    * auto: keep the same color range
                    * unspecified
                    * unknown
                    * limited
                    * tv
                    * mpeg
                    * full
                    * pc
                    * jpeg

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setrange",
            inputs=[self],
            named_arguments={
                "range": range,
            },
        )[0]

    def setsar(
        self,
        sar: str | None = None,
        ratio: str | None = None,
        r: str | None = None,
        max: int | None = None,
    ) -> "Stream":
        """Set the pixel sample aspect ratio.

        Args:
            sar (str): set sample (pixel) aspect ratio

                Defaults to 0.
            ratio (str): set sample (pixel) aspect ratio

                Defaults to 0.
            r (str): set sample (pixel) aspect ratio

                Defaults to 0.
            max (int): set max value for nominator or denominator in the ratio (from 1 to INT_MAX)

                Defaults to 100.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="setsar",
            inputs=[self],
            named_arguments={
                "sar": sar,
                "ratio": ratio,
                "r": r,
                "max": max,
            },
        )[0]

    def settb(self, expr: str | None = None, tb: str | None = None) -> "Stream":
        """Set timebase for the video output link.

        Args:
            expr (str): set expression determining the output timebase

                Defaults to intb.
            tb (str): set expression determining the output timebase

                Defaults to intb.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="settb",
            inputs=[self],
            named_arguments={
                "expr": expr,
                "tb": tb,
            },
        )[0]

    def shear(
        self,
        shx: float | None = None,
        shy: float | None = None,
        fillcolor: str | None = None,
        c: str | None = None,
        interp: Literal["nearest", "bilinear"] | int | None = None,
    ) -> "Stream":
        """Shear transform the input image.

        Args:
            shx (float): set x shear factor (from -2 to 2)

                Defaults to 0.
            shy (float): set y shear factor (from -2 to 2)

                Defaults to 0.
            fillcolor (str): set background fill color

                Defaults to black.
            c (str): set background fill color

                Defaults to black.
            interp (int | str): set interpolation (from 0 to 1)

                Allowed values:
                    * nearest: nearest neighbour
                    * bilinear: bilinear

                Defaults to bilinear.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="shear",
            inputs=[self],
            named_arguments={
                "shx": shx,
                "shy": shy,
                "fillcolor": fillcolor,
                "c": c,
                "interp": interp,
            },
        )[0]

    def showcqt(
        self,
        size: str | None = None,
        s: str | None = None,
        fps: str | None = None,
        rate: str | None = None,
        r: str | None = None,
        bar_h: int | None = None,
        axis_h: int | None = None,
        sono_h: int | None = None,
        fullhd: bool | None = None,
        sono_v: str | None = None,
        volume: str | None = None,
        bar_v: str | None = None,
        volume2: str | None = None,
        sono_g: float | None = None,
        gamma: float | None = None,
        bar_g: float | None = None,
        gamma2: float | None = None,
        bar_t: float | None = None,
        timeclamp: float | None = None,
        tc: float | None = None,
        attack: float | None = None,
        basefreq: float | None = None,
        endfreq: float | None = None,
        coeffclamp: float | None = None,
        tlength: str | None = None,
        count: int | None = None,
        fcount: int | None = None,
        fontfile: str | None = None,
        font: str | None = None,
        fontcolor: str | None = None,
        axisfile: str | None = None,
        axis: bool | None = None,
        text: bool | None = None,
        csp: Literal[
            "unspecified",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt2020ncl",
        ]
        | int
        | None = None,
        cscheme: str | None = None,
    ) -> "Stream":
        """Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output.

        Args:
            size (str): set video size

                Defaults to 1920x1080.
            s (str): set video size

                Defaults to 1920x1080.
            fps (str): set video rate

                Defaults to 25.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            bar_h (int): set bargraph height (from -1 to INT_MAX)

                Defaults to -1.
            axis_h (int): set axis height (from -1 to INT_MAX)

                Defaults to -1.
            sono_h (int): set sonogram height (from -1 to INT_MAX)

                Defaults to -1.
            fullhd (bool): set fullhd size

                Defaults to true.
            sono_v (str): set sonogram volume

                Defaults to 16.
            volume (str): set sonogram volume

                Defaults to 16.
            bar_v (str): set bargraph volume

                Defaults to sono_v.
            volume2 (str): set bargraph volume

                Defaults to sono_v.
            sono_g (float): set sonogram gamma (from 1 to 7)

                Defaults to 3.
            gamma (float): set sonogram gamma (from 1 to 7)

                Defaults to 3.
            bar_g (float): set bargraph gamma (from 1 to 7)

                Defaults to 1.
            gamma2 (float): set bargraph gamma (from 1 to 7)

                Defaults to 1.
            bar_t (float): set bar transparency (from 0 to 1)

                Defaults to 1.
            timeclamp (float): set timeclamp (from 0.002 to 1)

                Defaults to 0.17.
            tc (float): set timeclamp (from 0.002 to 1)

                Defaults to 0.17.
            attack (float): set attack time (from 0 to 1)

                Defaults to 0.
            basefreq (float): set base frequency (from 10 to 100000)

                Defaults to 20.0152.
            endfreq (float): set end frequency (from 10 to 100000)

                Defaults to 20495.6.
            coeffclamp (float): set coeffclamp (from 0.1 to 10)

                Defaults to 1.
            tlength (str): set tlength

                Defaults to 384*tc/(384+tc*f).
            count (int): set transform count (from 1 to 30)

                Defaults to 6.
            fcount (int): set frequency count (from 0 to 10)

                Defaults to 0.
            fontfile (str): set axis font file

            font (str): set axis font

            fontcolor (str): set font color

                Defaults to st(0, (midi(f)-59.5)/12);st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));r(1-ld(1)) + b(ld(1)).
            axisfile (str): set axis image

            axis (bool): draw axis

                Defaults to true.
            text (bool): draw axis

                Defaults to true.
            csp (int | str): set color space (from 0 to INT_MAX)

                Allowed values:
                    * unspecified: unspecified
                    * bt709: bt709
                    * fcc: fcc
                    * bt470bg: bt470bg
                    * smpte170m: smpte170m
                    * smpte240m: smpte240m
                    * bt2020ncl: bt2020ncl

                Defaults to unspecified.
            cscheme (str): set color scheme

                Defaults to 1|0.5|0|0|0.5|1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showcqt",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "fps": fps,
                "rate": rate,
                "r": r,
                "bar_h": bar_h,
                "axis_h": axis_h,
                "sono_h": sono_h,
                "fullhd": fullhd,
                "sono_v": sono_v,
                "volume": volume,
                "bar_v": bar_v,
                "volume2": volume2,
                "sono_g": sono_g,
                "gamma": gamma,
                "bar_g": bar_g,
                "gamma2": gamma2,
                "bar_t": bar_t,
                "timeclamp": timeclamp,
                "tc": tc,
                "attack": attack,
                "basefreq": basefreq,
                "endfreq": endfreq,
                "coeffclamp": coeffclamp,
                "tlength": tlength,
                "count": count,
                "fcount": fcount,
                "fontfile": fontfile,
                "font": font,
                "fontcolor": fontcolor,
                "axisfile": axisfile,
                "axis": axis,
                "text": text,
                "csp": csp,
                "cscheme": cscheme,
            },
        )[0]

    def showcwt(
        self,
        size: str | None = None,
        s: str | None = None,
        rate: str | None = None,
        r: str | None = None,
        scale: Literal[
            "linear", "log", "bark", "mel", "erbs", "sqrt", "cbrt", "qdrt", "fm"
        ]
        | int
        | None = None,
        iscale: Literal["linear", "log", "sqrt", "cbrt", "qdrt"] | int | None = None,
        min: float | None = None,
        max: float | None = None,
        imin: float | None = None,
        imax: float | None = None,
        logb: float | None = None,
        deviation: float | None = None,
        pps: int | None = None,
        mode: Literal["magnitude", "phase", "magphase", "channel", "stereo"]
        | int
        | None = None,
        slide: Literal["replace", "scroll", "frame"] | int | None = None,
        direction: Literal["lr", "rl", "ud", "du"] | int | None = None,
        bar: float | None = None,
        rotation: float | None = None,
    ) -> "Stream":
        """Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output.

        Args:
            size (str): set video size

                Defaults to 640x512.
            s (str): set video size

                Defaults to 640x512.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            scale (int | str): set frequency scale (from 0 to 8)

                Allowed values:
                    * linear: linear
                    * log: logarithmic
                    * bark: bark
                    * mel: mel
                    * erbs: erbs
                    * sqrt: sqrt
                    * cbrt: cbrt
                    * qdrt: qdrt
                    * fm: fm

                Defaults to linear.
            iscale (int | str): set intensity scale (from 0 to 4)

                Allowed values:
                    * linear: linear
                    * log: logarithmic
                    * sqrt: sqrt
                    * cbrt: cbrt
                    * qdrt: qdrt

                Defaults to log.
            min (float): set minimum frequency (from 1 to 192000)

                Defaults to 20.
            max (float): set maximum frequency (from 1 to 192000)

                Defaults to 20000.
            imin (float): set minimum intensity (from 0 to 1)

                Defaults to 0.
            imax (float): set maximum intensity (from 0 to 1)

                Defaults to 1.
            logb (float): set logarithmic basis (from 0 to 1)

                Defaults to 0.0001.
            deviation (float): set frequency deviation (from 0 to 100)

                Defaults to 1.
            pps (int): set pixels per second (from 1 to 1024)

                Defaults to 64.
            mode (int | str): set output mode (from 0 to 4)

                Allowed values:
                    * magnitude: magnitude
                    * phase: phase
                    * magphase: magnitude+phase
                    * channel: color per channel
                    * stereo: stereo difference

                Defaults to magnitude.
            slide (int | str): set slide mode (from 0 to 2)

                Allowed values:
                    * replace: replace
                    * scroll: scroll
                    * frame: frame

                Defaults to replace.
            direction (int | str): set direction mode (from 0 to 3)

                Allowed values:
                    * lr: left to right
                    * rl: right to left
                    * ud: up to down
                    * du: down to up

                Defaults to lr.
            bar (float): set bargraph ratio (from 0 to 1)

                Defaults to 0.
            rotation (float): set color rotation (from -1 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showcwt",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
                "scale": scale,
                "iscale": iscale,
                "min": min,
                "max": max,
                "imin": imin,
                "imax": imax,
                "logb": logb,
                "deviation": deviation,
                "pps": pps,
                "mode": mode,
                "slide": slide,
                "direction": direction,
                "bar": bar,
                "rotation": rotation,
            },
        )[0]

    def showfreqs(
        self,
        size: str | None = None,
        s: str | None = None,
        rate: str | None = None,
        r: str | None = None,
        mode: Literal["line", "bar", "dot"] | int | None = None,
        ascale: Literal["lin", "sqrt", "cbrt", "log"] | int | None = None,
        fscale: Literal["lin", "log", "rlog"] | int | None = None,
        win_size: int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        overlap: float | None = None,
        averaging: int | None = None,
        colors: str | None = None,
        cmode: Literal["combined", "separate"] | int | None = None,
        minamp: float | None = None,
        data: Literal["magnitude", "phase", "delay"] | int | None = None,
        channels: str | None = None,
    ) -> "Stream":
        """Convert input audio to a frequencies video output.

        Args:
            size (str): set video size

                Defaults to 1024x512.
            s (str): set video size

                Defaults to 1024x512.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            mode (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * line: show lines
                    * bar: show bars
                    * dot: show dots

                Defaults to bar.
            ascale (int | str): set amplitude scale (from 0 to 3)

                Allowed values:
                    * lin: linear
                    * sqrt: square root
                    * cbrt: cubic root
                    * log: logarithmic

                Defaults to log.
            fscale (int | str): set frequency scale (from 0 to 2)

                Allowed values:
                    * lin: linear
                    * log: logarithmic
                    * rlog: reverse logarithmic

                Defaults to lin.
            win_size (int): set window size (from 16 to 65536)

                Defaults to 2048.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 1.
            averaging (int): set time averaging (from 0 to INT_MAX)

                Defaults to 1.
            colors (str): set channels colors

                Defaults to red|green|blue|yellow|orange|lime|pink|magenta|brown.
            cmode (int | str): set channel mode (from 0 to 1)

                Allowed values:
                    * combined: show all channels in same window
                    * separate: show each channel in own window

                Defaults to combined.
            minamp (float): set minimum amplitude (from FLT_MIN to 1e-06)

                Defaults to 1e-06.
            data (int | str): set data mode (from 0 to 2)

                Allowed values:
                    * magnitude: show magnitude
                    * phase: show phase
                    * delay: show group delay

                Defaults to magnitude.
            channels (str): set channels to draw

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showfreqs",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "rate": rate,
                "r": r,
                "mode": mode,
                "ascale": ascale,
                "fscale": fscale,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
                "averaging": averaging,
                "colors": colors,
                "cmode": cmode,
                "minamp": minamp,
                "data": data,
                "channels": channels,
            },
        )[0]

    def showinfo(
        self, checksum: bool | None = None, udu_sei_as_ascii: bool | None = None
    ) -> "Stream":
        """Show textual information for each video frame.

        Args:
            checksum (bool): calculate checksums

                Defaults to true.
            udu_sei_as_ascii (bool): try to print user data unregistered SEI as ascii character when possible

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showinfo",
            inputs=[self],
            named_arguments={
                "checksum": checksum,
                "udu_sei_as_ascii": udu_sei_as_ascii,
            },
        )[0]

    def showpalette(self, s: int | None = None) -> "Stream":
        """Display frame palette.

        Args:
            s (int): set pixel box size (from 1 to 100)

                Defaults to 30.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showpalette",
            inputs=[self],
            named_arguments={
                "s": s,
            },
        )[0]

    def showspatial(
        self,
        size: str | None = None,
        s: str | None = None,
        win_size: int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        rate: str | None = None,
        r: str | None = None,
    ) -> "Stream":
        """Convert input audio to a spatial video output.

        Args:
            size (str): set video size

                Defaults to 512x512.
            s (str): set video size

                Defaults to 512x512.
            win_size (int): set window size (from 1024 to 65536)

                Defaults to 4096.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showspatial",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "win_size": win_size,
                "win_func": win_func,
                "rate": rate,
                "r": r,
            },
        )[0]

    def showspectrum(
        self,
        size: str | None = None,
        s: str | None = None,
        slide: Literal["replace", "scroll", "fullframe", "rscroll", "lreplace"]
        | int
        | None = None,
        mode: Literal["combined", "separate"] | int | None = None,
        color: Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | int
        | None = None,
        scale: Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"]
        | int
        | None = None,
        fscale: Literal["lin", "log"] | int | None = None,
        saturation: float | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        orientation: Literal["vertical", "horizontal"] | int | None = None,
        overlap: float | None = None,
        gain: float | None = None,
        data: Literal["magnitude", "phase", "uphase"] | int | None = None,
        rotation: float | None = None,
        start: int | None = None,
        stop: int | None = None,
        fps: str | None = None,
        legend: bool | None = None,
        drange: float | None = None,
        limit: float | None = None,
        opacity: float | None = None,
    ) -> "Stream":
        """Convert input audio to a spectrum video output.

        Args:
            size (str): set video size

                Defaults to 640x512.
            s (str): set video size

                Defaults to 640x512.
            slide (int | str): set sliding mode (from 0 to 4)

                Allowed values:
                    * replace: replace old columns with new
                    * scroll: scroll from right to left
                    * fullframe: return full frames
                    * rscroll: scroll from left to right
                    * lreplace: replace from right to left

                Defaults to replace.
            mode (int | str): set channel display mode (from 0 to 1)

                Allowed values:
                    * combined: combined mode
                    * separate: separate mode

                Defaults to combined.
            color (int | str): set channel coloring (from 0 to 14)

                Allowed values:
                    * channel: separate color for each channel
                    * intensity: intensity based coloring
                    * rainbow: rainbow based coloring
                    * moreland: moreland based coloring
                    * nebulae: nebulae based coloring
                    * fire: fire based coloring
                    * fiery: fiery based coloring
                    * fruit: fruit based coloring
                    * cool: cool based coloring
                    * magma: magma based coloring
                    * green: green based coloring
                    * viridis: viridis based coloring
                    * plasma: plasma based coloring
                    * cividis: cividis based coloring
                    * terrain: terrain based coloring

                Defaults to channel.
            scale (int | str): set display scale (from 0 to 5)

                Allowed values:
                    * lin: linear
                    * sqrt: square root
                    * cbrt: cubic root
                    * log: logarithmic
                    * 4thrt: 4th root
                    * 5thrt: 5th root

                Defaults to sqrt.
            fscale (int | str): set frequency scale (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: logarithmic

                Defaults to lin.
            saturation (float): color saturation multiplier (from -10 to 10)

                Defaults to 1.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            orientation (int | str): set orientation (from 0 to 1)

                Allowed values:
                    * vertical
                    * horizontal

                Defaults to vertical.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 0.
            gain (float): set scale gain (from 0 to 128)

                Defaults to 1.
            data (int | str): set data mode (from 0 to 2)

                Allowed values:
                    * magnitude
                    * phase
                    * uphase

                Defaults to magnitude.
            rotation (float): color rotation (from -1 to 1)

                Defaults to 0.
            start (int): start frequency (from 0 to INT_MAX)

                Defaults to 0.
            stop (int): stop frequency (from 0 to INT_MAX)

                Defaults to 0.
            fps (str): set video rate

                Defaults to auto.
            legend (bool): draw legend

                Defaults to false.
            drange (float): set dynamic range in dBFS (from 10 to 200)

                Defaults to 120.
            limit (float): set upper limit in dBFS (from -100 to 100)

                Defaults to 0.
            opacity (float): set opacity strength (from 0 to 10)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showspectrum",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "slide": slide,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "overlap": overlap,
                "gain": gain,
                "data": data,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "fps": fps,
                "legend": legend,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            },
        )[0]

    def showspectrumpic(
        self,
        size: str | None = None,
        s: str | None = None,
        mode: Literal["combined", "separate"] | int | None = None,
        color: Literal[
            "channel",
            "intensity",
            "rainbow",
            "moreland",
            "nebulae",
            "fire",
            "fiery",
            "fruit",
            "cool",
            "magma",
            "green",
            "viridis",
            "plasma",
            "cividis",
            "terrain",
        ]
        | int
        | None = None,
        scale: Literal["lin", "sqrt", "cbrt", "log", "4thrt", "5thrt"]
        | int
        | None = None,
        fscale: Literal["lin", "log"] | int | None = None,
        saturation: float | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        orientation: Literal["vertical", "horizontal"] | int | None = None,
        gain: float | None = None,
        legend: bool | None = None,
        rotation: float | None = None,
        start: int | None = None,
        stop: int | None = None,
        drange: float | None = None,
        limit: float | None = None,
        opacity: float | None = None,
    ) -> "Stream":
        """Convert input audio to a spectrum video output single picture.

        Args:
            size (str): set video size

                Defaults to 4096x2048.
            s (str): set video size

                Defaults to 4096x2048.
            mode (int | str): set channel display mode (from 0 to 1)

                Allowed values:
                    * combined: combined mode
                    * separate: separate mode

                Defaults to combined.
            color (int | str): set channel coloring (from 0 to 14)

                Allowed values:
                    * channel: separate color for each channel
                    * intensity: intensity based coloring
                    * rainbow: rainbow based coloring
                    * moreland: moreland based coloring
                    * nebulae: nebulae based coloring
                    * fire: fire based coloring
                    * fiery: fiery based coloring
                    * fruit: fruit based coloring
                    * cool: cool based coloring
                    * magma: magma based coloring
                    * green: green based coloring
                    * viridis: viridis based coloring
                    * plasma: plasma based coloring
                    * cividis: cividis based coloring
                    * terrain: terrain based coloring

                Defaults to intensity.
            scale (int | str): set display scale (from 0 to 5)

                Allowed values:
                    * lin: linear
                    * sqrt: square root
                    * cbrt: cubic root
                    * log: logarithmic
                    * 4thrt: 4th root
                    * 5thrt: 5th root

                Defaults to log.
            fscale (int | str): set frequency scale (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: logarithmic

                Defaults to lin.
            saturation (float): color saturation multiplier (from -10 to 10)

                Defaults to 1.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            orientation (int | str): set orientation (from 0 to 1)

                Allowed values:
                    * vertical
                    * horizontal

                Defaults to vertical.
            gain (float): set scale gain (from 0 to 128)

                Defaults to 1.
            legend (bool): draw legend

                Defaults to true.
            rotation (float): color rotation (from -1 to 1)

                Defaults to 0.
            start (int): start frequency (from 0 to INT_MAX)

                Defaults to 0.
            stop (int): stop frequency (from 0 to INT_MAX)

                Defaults to 0.
            drange (float): set dynamic range in dBFS (from 10 to 200)

                Defaults to 120.
            limit (float): set upper limit in dBFS (from -100 to 100)

                Defaults to 0.
            opacity (float): set opacity strength (from 0 to 10)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showspectrumpic",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "color": color,
                "scale": scale,
                "fscale": fscale,
                "saturation": saturation,
                "win_func": win_func,
                "orientation": orientation,
                "gain": gain,
                "legend": legend,
                "rotation": rotation,
                "start": start,
                "stop": stop,
                "drange": drange,
                "limit": limit,
                "opacity": opacity,
            },
        )[0]

    def showvolume(
        self,
        rate: str | None = None,
        r: str | None = None,
        b: int | None = None,
        w: int | None = None,
        h: int | None = None,
        f: float | None = None,
        c: str | None = None,
        t: bool | None = None,
        v: bool | None = None,
        dm: float | None = None,
        dmc: str | None = None,
        o: Literal["h", "v"] | int | None = None,
        s: int | None = None,
        p: float | None = None,
        m: Literal["p", "r"] | int | None = None,
        ds: Literal["lin", "log"] | int | None = None,
    ) -> "Stream":
        """Convert input audio volume to video output.

        Args:
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            b (int): set border width (from 0 to 5)

                Defaults to 1.
            w (int): set channel width (from 80 to 8192)

                Defaults to 400.
            h (int): set channel height (from 1 to 900)

                Defaults to 20.
            f (float): set fade (from 0 to 1)

                Defaults to 0.95.
            c (str): set volume color expression

                Defaults to PEAK*255+floor((1-PEAK)*255)*256+0xff000000.
            t (bool): display channel names

                Defaults to true.
            v (bool): display volume value

                Defaults to true.
            dm (float): duration for max value display (from 0 to 9000)

                Defaults to 0.
            dmc (str): set color of the max value line

                Defaults to orange.
            o (int | str): set orientation (from 0 to 1)

                Allowed values:
                    * h: horizontal
                    * v: vertical

                Defaults to h.
            s (int): set step size (from 0 to 5)

                Defaults to 0.
            p (float): set background opacity (from 0 to 1)

                Defaults to 0.
            m (int | str): set mode (from 0 to 1)

                Allowed values:
                    * p: peak
                    * r: rms

                Defaults to p.
            ds (int | str): set display scale (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: log

                Defaults to lin.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showvolume",
            inputs=[self],
            named_arguments={
                "rate": rate,
                "r": r,
                "b": b,
                "w": w,
                "h": h,
                "f": f,
                "c": c,
                "t": t,
                "v": v,
                "dm": dm,
                "dmc": dmc,
                "o": o,
                "s": s,
                "p": p,
                "m": m,
                "ds": ds,
            },
        )[0]

    def showwaves(
        self,
        size: str | None = None,
        s: str | None = None,
        mode: Literal["point", "line", "p2p", "cline"] | int | None = None,
        n: str | None = None,
        rate: str | None = None,
        r: str | None = None,
        split_channels: bool | None = None,
        colors: str | None = None,
        scale: Literal["lin", "log", "sqrt", "cbrt"] | int | None = None,
        draw: Literal["scale", "full"] | int | None = None,
    ) -> "Stream":
        """Convert input audio to a video output.

        Args:
            size (str): set video size

                Defaults to 600x240.
            s (str): set video size

                Defaults to 600x240.
            mode (int | str): select display mode (from 0 to 3)

                Allowed values:
                    * point: draw a point for each sample
                    * line: draw a line for each sample
                    * p2p: draw a line between samples
                    * cline: draw a centered line for each sample

                Defaults to point.
            n (str): set how many samples to show in the same point (from 0 to INT_MAX)

                Defaults to 0/1.
            rate (str): set video rate

                Defaults to 25.
            r (str): set video rate

                Defaults to 25.
            split_channels (bool): draw channels separately

                Defaults to false.
            colors (str): set channels colors

                Defaults to red|green|blue|yellow|orange|lime|pink|magenta|brown.
            scale (int | str): set amplitude scale (from 0 to 3)

                Allowed values:
                    * lin: linear
                    * log: logarithmic
                    * sqrt: square root
                    * cbrt: cubic root

                Defaults to lin.
            draw (int | str): set draw mode (from 0 to 1)

                Allowed values:
                    * scale: scale pixel values for each drawn sample
                    * full: draw every pixel for sample directly

                Defaults to scale.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showwaves",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "mode": mode,
                "n": n,
                "rate": rate,
                "r": r,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
            },
        )[0]

    def showwavespic(
        self,
        size: str | None = None,
        s: str | None = None,
        split_channels: bool | None = None,
        colors: str | None = None,
        scale: Literal["lin", "log", "sqrt", "cbrt"] | int | None = None,
        draw: Literal["scale", "full"] | int | None = None,
        filter: Literal["average", "peak"] | int | None = None,
    ) -> "Stream":
        """Convert input audio to a video output single picture.

        Args:
            size (str): set video size

                Defaults to 600x240.
            s (str): set video size

                Defaults to 600x240.
            split_channels (bool): draw channels separately

                Defaults to false.
            colors (str): set channels colors

                Defaults to red|green|blue|yellow|orange|lime|pink|magenta|brown.
            scale (int | str): set amplitude scale (from 0 to 3)

                Allowed values:
                    * lin: linear
                    * log: logarithmic
                    * sqrt: square root
                    * cbrt: cubic root

                Defaults to lin.
            draw (int | str): set draw mode (from 0 to 1)

                Allowed values:
                    * scale: scale pixel values for each drawn sample
                    * full: draw every pixel for sample directly

                Defaults to scale.
            filter (int | str): set filter mode (from 0 to 1)

                Allowed values:
                    * average: use average samples
                    * peak: use peak samples

                Defaults to average.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="showwavespic",
            inputs=[self],
            named_arguments={
                "size": size,
                "s": s,
                "split_channels": split_channels,
                "colors": colors,
                "scale": scale,
                "draw": draw,
                "filter": filter,
            },
        )[0]

    def shuffleframes(self, mapping: str | None = None) -> "Stream":
        """Shuffle video frames.

        Args:
            mapping (str): set destination indexes of input frames

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="shuffleframes",
            inputs=[self],
            named_arguments={
                "mapping": mapping,
            },
        )[0]

    def shufflepixels(
        self,
        direction: Literal["forward", "inverse"] | int | None = None,
        d: Literal["forward", "inverse"] | int | None = None,
        mode: Literal["horizontal", "vertical", "block"] | int | None = None,
        m: Literal["horizontal", "vertical", "block"] | int | None = None,
        width: int | None = None,
        w: int | None = None,
        height: int | None = None,
        h: int | None = None,
        seed: str | None = None,
        s: str | None = None,
    ) -> "Stream":
        """Shuffle video pixels.

        Args:
            direction (int | str): set shuffle direction (from 0 to 1)

                Allowed values:
                    * forward
                    * inverse

                Defaults to forward.
            d (int | str): set shuffle direction (from 0 to 1)

                Allowed values:
                    * forward
                    * inverse

                Defaults to forward.
            mode (int | str): set shuffle mode (from 0 to 2)

                Allowed values:
                    * horizontal
                    * vertical
                    * block

                Defaults to horizontal.
            m (int | str): set shuffle mode (from 0 to 2)

                Allowed values:
                    * horizontal
                    * vertical
                    * block

                Defaults to horizontal.
            width (int): set block width (from 1 to 8000)

                Defaults to 10.
            w (int): set block width (from 1 to 8000)

                Defaults to 10.
            height (int): set block height (from 1 to 8000)

                Defaults to 10.
            h (int): set block height (from 1 to 8000)

                Defaults to 10.
            seed (str): set random seed (from -1 to UINT32_MAX)

                Defaults to -1.
            s (str): set random seed (from -1 to UINT32_MAX)

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="shufflepixels",
            inputs=[self],
            named_arguments={
                "direction": direction,
                "d": d,
                "mode": mode,
                "m": m,
                "width": width,
                "w": w,
                "height": height,
                "h": h,
                "seed": seed,
                "s": s,
            },
        )[0]

    def shuffleplanes(
        self,
        map0: int | None = None,
        map1: int | None = None,
        map2: int | None = None,
        map3: int | None = None,
    ) -> "Stream":
        """Shuffle video planes.

        Args:
            map0 (int): Index of the input plane to be used as the first output plane  (from 0 to 3)

                Defaults to 0.
            map1 (int): Index of the input plane to be used as the second output plane  (from 0 to 3)

                Defaults to 1.
            map2 (int): Index of the input plane to be used as the third output plane  (from 0 to 3)

                Defaults to 2.
            map3 (int): Index of the input plane to be used as the fourth output plane  (from 0 to 3)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="shuffleplanes",
            inputs=[self],
            named_arguments={
                "map0": map0,
                "map1": map1,
                "map2": map2,
                "map3": map3,
            },
        )[0]

    def sidechaincompress(
        self,
        sidechain_stream: "Stream",
        level_in: float | None = None,
        mode: Literal["downward", "upward"] | int | None = None,
        threshold: float | None = None,
        ratio: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        makeup: float | None = None,
        knee: float | None = None,
        link: Literal["average", "maximum"] | int | None = None,
        detection: Literal["peak", "rms"] | int | None = None,
        level_sc: float | None = None,
        mix: float | None = None,
    ) -> "Stream":
        """Sidechain compressor.

        Args:
            sidechain_stream (Stream): Input audio stream.
            level_in (float): set input gain (from 0.015625 to 64)

                Defaults to 1.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * downward
                    * upward

                Defaults to downward.
            threshold (float): set threshold (from 0.000976563 to 1)

                Defaults to 0.125.
            ratio (float): set ratio (from 1 to 20)

                Defaults to 2.
            attack (float): set attack (from 0.01 to 2000)

                Defaults to 20.
            release (float): set release (from 0.01 to 9000)

                Defaults to 250.
            makeup (float): set make up gain (from 1 to 64)

                Defaults to 1.
            knee (float): set knee (from 1 to 8)

                Defaults to 2.82843.
            link (int | str): set link type (from 0 to 1)

                Allowed values:
                    * average
                    * maximum

                Defaults to average.
            detection (int | str): set detection (from 0 to 1)

                Allowed values:
                    * peak
                    * rms

                Defaults to rms.
            level_sc (float): set sidechain gain (from 0.015625 to 64)

                Defaults to 1.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sidechaincompress",
            inputs=[self, sidechain_stream],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "link": link,
                "detection": detection,
                "level_sc": level_sc,
                "mix": mix,
            },
        )[0]

    def sidechaingate(
        self,
        sidechain_stream: "Stream",
        level_in: float | None = None,
        mode: Literal["downward", "upward"] | int | None = None,
        range: float | None = None,
        threshold: float | None = None,
        ratio: float | None = None,
        attack: float | None = None,
        release: float | None = None,
        makeup: float | None = None,
        knee: float | None = None,
        detection: Literal["peak", "rms"] | int | None = None,
        link: Literal["average", "maximum"] | int | None = None,
        level_sc: float | None = None,
    ) -> "Stream":
        """Audio sidechain gate.

        Args:
            sidechain_stream (Stream): Input audio stream.
            level_in (float): set input level (from 0.015625 to 64)

                Defaults to 1.
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * downward
                    * upward

                Defaults to downward.
            range (float): set max gain reduction (from 0 to 1)

                Defaults to 0.06125.
            threshold (float): set threshold (from 0 to 1)

                Defaults to 0.125.
            ratio (float): set ratio (from 1 to 9000)

                Defaults to 2.
            attack (float): set attack (from 0.01 to 9000)

                Defaults to 20.
            release (float): set release (from 0.01 to 9000)

                Defaults to 250.
            makeup (float): set makeup gain (from 1 to 64)

                Defaults to 1.
            knee (float): set knee (from 1 to 8)

                Defaults to 2.82843.
            detection (int | str): set detection (from 0 to 1)

                Allowed values:
                    * peak
                    * rms

                Defaults to rms.
            link (int | str): set link (from 0 to 1)

                Allowed values:
                    * average
                    * maximum

                Defaults to average.
            level_sc (float): set sidechain gain (from 0.015625 to 64)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sidechaingate",
            inputs=[self, sidechain_stream],
            named_arguments={
                "level_in": level_in,
                "mode": mode,
                "range": range,
                "threshold": threshold,
                "ratio": ratio,
                "attack": attack,
                "release": release,
                "makeup": makeup,
                "knee": knee,
                "detection": detection,
                "link": link,
                "level_sc": level_sc,
            },
        )[0]

    def sidedata(
        self,
        mode: Literal["select", "delete"] | int | None = None,
        type: Literal[
            "PANSCAN",
            "A53_CC",
            "STEREO3D",
            "MATRIXENCODING",
            "DOWNMIX_INFO",
            "REPLAYGAIN",
            "DISPLAYMATRIX",
            "AFD",
            "MOTION_VECTORS",
            "SKIP_SAMPLES",
            "AUDIO_SERVICE_TYPE",
            "MASTERING_DISPLAY_METADATA",
            "GOP_TIMECODE",
            "SPHERICAL",
            "CONTENT_LIGHT_LEVEL",
            "ICC_PROFILE",
            "S12M_TIMECOD",
            "DYNAMIC_HDR_PLUS",
            "REGIONS_OF_INTEREST",
            "VIDEO_ENC_PARAMS",
            "SEI_UNREGISTERED",
            "FILM_GRAIN_PARAMS",
            "DETECTION_BOUNDING_BOXES",
            "DETECTION_BBOXES",
            "DOVI_RPU_BUFFER",
            "DOVI_METADATA",
            "DYNAMIC_HDR_VIVID",
            "AMBIENT_VIEWING_ENVIRONMENT",
            "VIDEO_HINT",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Manipulate video frame side data.

        Args:
            mode (int | str): set a mode of operation (from 0 to 1)

                Allowed values:
                    * select: select frame
                    * delete: delete side data

                Defaults to select.
            type (int | str): set side data type (from -1 to INT_MAX)

                Allowed values:
                    * PANSCAN
                    * A53_CC
                    * STEREO3D
                    * MATRIXENCODING
                    * DOWNMIX_INFO
                    * REPLAYGAIN
                    * DISPLAYMATRIX
                    * AFD
                    * MOTION_VECTORS
                    * SKIP_SAMPLES
                    * AUDIO_SERVICE_TYPE
                    * MASTERING_DISPLAY_METADATA
                    * GOP_TIMECODE
                    * SPHERICAL
                    * CONTENT_LIGHT_LEVEL
                    * ICC_PROFILE
                    * S12M_TIMECOD
                    * DYNAMIC_HDR_PLUS
                    * REGIONS_OF_INTEREST
                    * VIDEO_ENC_PARAMS
                    * SEI_UNREGISTERED
                    * FILM_GRAIN_PARAMS
                    * DETECTION_BOUNDING_BOXES
                    * DETECTION_BBOXES
                    * DOVI_RPU_BUFFER
                    * DOVI_METADATA
                    * DYNAMIC_HDR_VIVID
                    * AMBIENT_VIEWING_ENVIRONMENT
                    * VIDEO_HINT

                Defaults to -1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sidedata",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "type": type,
            },
        )[0]

    def signalstats(
        self,
        stat: Literal["tout", "vrep", "brng"] | None = None,
        out: Literal["tout", "vrep", "brng"] | int | None = None,
        c: str | None = None,
        color: str | None = None,
    ) -> "Stream":
        """Generate statistics from video analysis.

        Args:
            stat (str): set statistics filters

                Allowed values:
                    * tout: pixels for temporal outliers
                    * vrep: video lines for vertical line repetition
                    * brng: for pixels outside of broadcast range

                Defaults to 0.
            out (int | str): set video filter (from -1 to 2)

                Allowed values:
                    * tout: highlight pixels that depict temporal outliers
                    * vrep: highlight video lines that depict vertical line repetition
                    * brng: highlight pixels that are outside of broadcast range

                Defaults to -1.
            c (str): set highlight color

                Defaults to yellow.
            color (str): set highlight color

                Defaults to yellow.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="signalstats",
            inputs=[self],
            named_arguments={
                "stat": stat,
                "out": out,
                "c": c,
                "color": color,
            },
        )[0]

    def signature(
        self,
        *streams: "Stream",
        detectmode: Literal["off", "full", "fast"] | int | None = None,
        nb_inputs: int | None = None,
        filename: str | None = None,
        format: Literal["binary", "xml"] | int | None = None,
        th_d: int | None = None,
        th_dc: int | None = None,
        th_xh: int | None = None,
        th_di: int | None = None,
        th_it: float | None = None,
    ) -> "Stream":
        """Calculate the MPEG-7 video signature

        Args:
            *streams (Stream): One or more input streams.
            detectmode (int | str): set the detectmode (from 0 to 2)

                Allowed values:
                    * off
                    * full
                    * fast

                Defaults to off.
            nb_inputs (int): number of inputs (from 1 to INT_MAX)

                Defaults to 1.
            filename (str): filename for output files

            format (int | str): set output format (from 0 to 1)

                Allowed values:
                    * binary
                    * xml

                Defaults to binary.
            th_d (int): threshold to detect one word as similar (from 1 to INT_MAX)

                Defaults to 9000.
            th_dc (int): threshold to detect all words as similar (from 1 to INT_MAX)

                Defaults to 60000.
            th_xh (int): threshold to detect frames as similar (from 1 to INT_MAX)

                Defaults to 116.
            th_di (int): minimum length of matching sequence in frames (from 0 to INT_MAX)

                Defaults to 0.
            th_it (float): threshold for relation of good to all frames (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="signature",
            inputs=[self, *streams],
            named_arguments={
                "detectmode": detectmode,
                "nb_inputs": nb_inputs,
                "filename": filename,
                "format": format,
                "th_d": th_d,
                "th_dc": th_dc,
                "th_xh": th_xh,
                "th_di": th_di,
                "th_it": th_it,
            },
        )[0]

    def silencedetect(
        self,
        n: float | None = None,
        noise: float | None = None,
        d: str | None = None,
        duration: str | None = None,
        mono: bool | None = None,
        m: bool | None = None,
    ) -> "Stream":
        """Detect silence.

        Args:
            n (float): set noise tolerance (from 0 to DBL_MAX)

                Defaults to 0.001.
            noise (float): set noise tolerance (from 0 to DBL_MAX)

                Defaults to 0.001.
            d (str): set minimum duration in seconds

                Defaults to 2.
            duration (str): set minimum duration in seconds

                Defaults to 2.
            mono (bool): check each channel separately

                Defaults to false.
            m (bool): check each channel separately

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="silencedetect",
            inputs=[self],
            named_arguments={
                "n": n,
                "noise": noise,
                "d": d,
                "duration": duration,
                "mono": mono,
                "m": m,
            },
        )[0]

    def silenceremove(
        self,
        start_periods: int | None = None,
        start_duration: str | None = None,
        start_threshold: float | None = None,
        start_silence: str | None = None,
        start_mode: Literal["any", "all"] | int | None = None,
        stop_periods: int | None = None,
        stop_duration: str | None = None,
        stop_threshold: float | None = None,
        stop_silence: str | None = None,
        stop_mode: Literal["any", "all"] | int | None = None,
        detection: Literal["avg", "rms", "peak", "median", "ptp", "dev"]
        | int
        | None = None,
        window: str | None = None,
        timestamp: Literal["write", "copy"] | int | None = None,
    ) -> "Stream":
        """Remove silence.

        Args:
            start_periods (int): set periods of silence parts to skip from start (from 0 to 9000)

                Defaults to 0.
            start_duration (str): set start duration of non-silence part

                Defaults to 0.
            start_threshold (float): set threshold for start silence detection (from 0 to DBL_MAX)

                Defaults to 0.
            start_silence (str): set start duration of silence part to keep

                Defaults to 0.
            start_mode (int | str): set which channel will trigger trimming from start (from 0 to 1)

                Allowed values:
                    * any
                    * all

                Defaults to any.
            stop_periods (int): set periods of silence parts to skip from end (from -9000 to 9000)

                Defaults to 0.
            stop_duration (str): set stop duration of silence part

                Defaults to 0.
            stop_threshold (float): set threshold for stop silence detection (from 0 to DBL_MAX)

                Defaults to 0.
            stop_silence (str): set stop duration of silence part to keep

                Defaults to 0.
            stop_mode (int | str): set which channel will trigger trimming from end (from 0 to 1)

                Allowed values:
                    * any
                    * all

                Defaults to all.
            detection (int | str): set how silence is detected (from 0 to 5)

                Allowed values:
                    * avg: use mean absolute values of samples
                    * rms: use root mean squared values of samples
                    * peak: use max absolute values of samples
                    * median: use median of absolute values of samples
                    * ptp: use absolute of max peak to min peak difference
                    * dev: use standard deviation from values of samples

                Defaults to rms.
            window (str): set duration of window for silence detection

                Defaults to 0.02.
            timestamp (int | str): set how every output frame timestamp is processed (from 0 to 1)

                Allowed values:
                    * write: full timestamps rewrite, keep only the start time
                    * copy: non-dropped frames are left with same timestamp

                Defaults to write.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="silenceremove",
            inputs=[self],
            named_arguments={
                "start_periods": start_periods,
                "start_duration": start_duration,
                "start_threshold": start_threshold,
                "start_silence": start_silence,
                "start_mode": start_mode,
                "stop_periods": stop_periods,
                "stop_duration": stop_duration,
                "stop_threshold": stop_threshold,
                "stop_silence": stop_silence,
                "stop_mode": stop_mode,
                "detection": detection,
                "window": window,
                "timestamp": timestamp,
            },
        )[0]

    def siti(self, print_summary: bool | None = None) -> "Stream":
        """Calculate spatial information (SI) and temporal information (TI).

        Args:
            print_summary (bool): Print summary showing average values

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="siti",
            inputs=[self],
            named_arguments={
                "print_summary": print_summary,
            },
        )[0]

    def smartblur(
        self,
        luma_radius: float | None = None,
        lr: float | None = None,
        luma_strength: float | None = None,
        ls: float | None = None,
        luma_threshold: int | None = None,
        lt: int | None = None,
        chroma_radius: float | None = None,
        cr: float | None = None,
        chroma_strength: float | None = None,
        cs: float | None = None,
        chroma_threshold: int | None = None,
        ct: int | None = None,
        alpha_radius: float | None = None,
        ar: float | None = None,
        alpha_strength: float | None = None,
        as_: float | None = None,
        alpha_threshold: int | None = None,
        at: int | None = None,
    ) -> "Stream":
        """Blur the input video without impacting the outlines.

        Args:
            luma_radius (float): set luma radius (from 0.1 to 5)

                Defaults to 1.
            lr (float): set luma radius (from 0.1 to 5)

                Defaults to 1.
            luma_strength (float): set luma strength (from -1 to 1)

                Defaults to 1.
            ls (float): set luma strength (from -1 to 1)

                Defaults to 1.
            luma_threshold (int): set luma threshold (from -30 to 30)

                Defaults to 0.
            lt (int): set luma threshold (from -30 to 30)

                Defaults to 0.
            chroma_radius (float): set chroma radius (from -0.9 to 5)

                Defaults to -0.9.
            cr (float): set chroma radius (from -0.9 to 5)

                Defaults to -0.9.
            chroma_strength (float): set chroma strength (from -2 to 1)

                Defaults to -2.
            cs (float): set chroma strength (from -2 to 1)

                Defaults to -2.
            chroma_threshold (int): set chroma threshold (from -31 to 30)

                Defaults to -31.
            ct (int): set chroma threshold (from -31 to 30)

                Defaults to -31.
            alpha_radius (float): set alpha radius (from -0.9 to 5)

                Defaults to -0.9.
            ar (float): set alpha radius (from -0.9 to 5)

                Defaults to -0.9.
            alpha_strength (float): set alpha strength (from -2 to 1)

                Defaults to -2.
            as_ (float): set alpha strength (from -2 to 1)

                Defaults to -2.
            alpha_threshold (int): set alpha threshold (from -31 to 30)

                Defaults to -31.
            at (int): set alpha threshold (from -31 to 30)

                Defaults to -31.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="smartblur",
            inputs=[self],
            named_arguments={
                "luma_radius": luma_radius,
                "lr": lr,
                "luma_strength": luma_strength,
                "ls": ls,
                "luma_threshold": luma_threshold,
                "lt": lt,
                "chroma_radius": chroma_radius,
                "cr": cr,
                "chroma_strength": chroma_strength,
                "cs": cs,
                "chroma_threshold": chroma_threshold,
                "ct": ct,
                "alpha_radius": alpha_radius,
                "ar": ar,
                "alpha_strength": alpha_strength,
                "as": as_,
                "alpha_threshold": alpha_threshold,
                "at": at,
            },
        )[0]

    def sobel(
        self,
        planes: int | None = None,
        scale: float | None = None,
        delta: float | None = None,
    ) -> "Stream":
        """Apply sobel operator.

        Args:
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            scale (float): set scale (from 0 to 65535)

                Defaults to 1.
            delta (float): set delta (from -65535 to 65535)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="sobel",
            inputs=[self],
            named_arguments={
                "planes": planes,
                "scale": scale,
                "delta": delta,
            },
        )[0]

    def spectrumsynth(
        self,
        phase_stream: "Stream",
        sample_rate: int | None = None,
        channels: int | None = None,
        scale: Literal["lin", "log"] | int | None = None,
        slide: Literal["replace", "scroll", "fullframe", "rscroll"] | int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        overlap: float | None = None,
        orientation: Literal["vertical", "horizontal"] | int | None = None,
    ) -> "Stream":
        """Convert input spectrum videos to audio output.

        Args:
            phase_stream (Stream): Input video stream.
            sample_rate (int): set sample rate (from 15 to INT_MAX)

                Defaults to 44100.
            channels (int): set channels (from 1 to 8)

                Defaults to 1.
            scale (int | str): set input amplitude scale (from 0 to 1)

                Allowed values:
                    * lin: linear
                    * log: logarithmic

                Defaults to log.
            slide (int | str): set input sliding mode (from 0 to 3)

                Allowed values:
                    * replace: consume old columns with new
                    * scroll: consume only most right column
                    * fullframe: consume full frames
                    * rscroll: consume only most left column

                Defaults to fullframe.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to rect.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 1.
            orientation (int | str): set orientation (from 0 to 1)

                Allowed values:
                    * vertical
                    * horizontal

                Defaults to vertical.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="spectrumsynth",
            inputs=[self, phase_stream],
            named_arguments={
                "sample_rate": sample_rate,
                "channels": channels,
                "scale": scale,
                "slide": slide,
                "win_func": win_func,
                "overlap": overlap,
                "orientation": orientation,
            },
        )[0]

    def speechnorm(
        self,
        peak: float | None = None,
        p: float | None = None,
        expansion: float | None = None,
        e: float | None = None,
        compression: float | None = None,
        c: float | None = None,
        threshold: float | None = None,
        t: float | None = None,
        raise_: float | None = None,
        r: float | None = None,
        fall: float | None = None,
        f: float | None = None,
        channels: str | None = None,
        h: str | None = None,
        invert: bool | None = None,
        i: bool | None = None,
        link: bool | None = None,
        l: bool | None = None,
        rms: float | None = None,
        m: float | None = None,
    ) -> "Stream":
        """Speech Normalizer.

        Args:
            peak (float): set the peak value (from 0 to 1)

                Defaults to 0.95.
            p (float): set the peak value (from 0 to 1)

                Defaults to 0.95.
            expansion (float): set the max expansion factor (from 1 to 50)

                Defaults to 2.
            e (float): set the max expansion factor (from 1 to 50)

                Defaults to 2.
            compression (float): set the max compression factor (from 1 to 50)

                Defaults to 2.
            c (float): set the max compression factor (from 1 to 50)

                Defaults to 2.
            threshold (float): set the threshold value (from 0 to 1)

                Defaults to 0.
            t (float): set the threshold value (from 0 to 1)

                Defaults to 0.
            raise_ (float): set the expansion raising amount (from 0 to 1)

                Defaults to 0.001.
            r (float): set the expansion raising amount (from 0 to 1)

                Defaults to 0.001.
            fall (float): set the compression raising amount (from 0 to 1)

                Defaults to 0.001.
            f (float): set the compression raising amount (from 0 to 1)

                Defaults to 0.001.
            channels (str): set channels to filter

                Defaults to all.
            h (str): set channels to filter

                Defaults to all.
            invert (bool): set inverted filtering

                Defaults to false.
            i (bool): set inverted filtering

                Defaults to false.
            link (bool): set linked channels filtering

                Defaults to false.
            l (bool): set linked channels filtering

                Defaults to false.
            rms (float): set the RMS value (from 0 to 1)

                Defaults to 0.
            m (float): set the RMS value (from 0 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="speechnorm",
            inputs=[self],
            named_arguments={
                "peak": peak,
                "p": p,
                "expansion": expansion,
                "e": e,
                "compression": compression,
                "c": c,
                "threshold": threshold,
                "t": t,
                "raise": raise_,
                "r": r,
                "fall": fall,
                "f": f,
                "channels": channels,
                "h": h,
                "invert": invert,
                "i": i,
                "link": link,
                "l": l,
                "rms": rms,
                "m": m,
            },
        )[0]

    def split(self, outputs: int | None = None) -> "FilterMultiOutput":
        """Pass on the input to N video outputs.

        Args:
            outputs (int): set number of outputs (from 1 to INT_MAX)

                Defaults to 2.

        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="split",
            inputs=[self],
            named_arguments={
                "outputs": outputs,
            },
        )

    def spp(
        self,
        quality: int | None = None,
        qp: int | None = None,
        mode: Literal["hard", "soft"] | int | None = None,
        use_bframe_qp: bool | None = None,
    ) -> "Stream":
        """Apply a simple post processing filter.

        Args:
            quality (int): set quality (from 0 to 6)

                Defaults to 3.
            qp (int): force a constant quantizer parameter (from 0 to 63)

                Defaults to 0.
            mode (int | str): set thresholding mode (from 0 to 1)

                Allowed values:
                    * hard: hard thresholding
                    * soft: soft thresholding

                Defaults to hard.
            use_bframe_qp (bool): use B-frames' QP

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="spp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "mode": mode,
                "use_bframe_qp": use_bframe_qp,
            },
        )[0]

    def ssim(
        self,
        reference_stream: "Stream",
        stats_file: str | None = None,
        f: str | None = None,
    ) -> "Stream":
        """Calculate the SSIM between two video streams.

        Args:
            reference_stream (Stream): Input video stream.
            stats_file (str): Set file where to store per-frame difference information

            f (str): Set file where to store per-frame difference information


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ssim",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
            },
        )[0]

    def ssim360(
        self,
        reference_stream: "Stream",
        stats_file: str | None = None,
        f: str | None = None,
        compute_chroma: int | None = None,
        frame_skip_ratio: int | None = None,
        ref_projection: Literal[
            "e", "equirect", "c3x2", "c2x3", "barrel", "barrelsplit"
        ]
        | int
        | None = None,
        main_projection: Literal[
            "e", "equirect", "c3x2", "c2x3", "barrel", "barrelsplit"
        ]
        | int
        | None = None,
        ref_stereo: Literal["mono", "tb", "lr"] | int | None = None,
        main_stereo: Literal["mono", "tb", "lr"] | int | None = None,
        ref_pad: float | None = None,
        main_pad: float | None = None,
        use_tape: int | None = None,
        heatmap_str: str | None = None,
        default_heatmap_width: int | None = None,
        default_heatmap_height: int | None = None,
    ) -> "Stream":
        """Calculate the SSIM between two 360 video streams.

        Args:
            reference_stream (Stream): Input video stream.
            stats_file (str): Set file where to store per-frame difference information

            f (str): Set file where to store per-frame difference information

            compute_chroma (int): Specifies if non-luma channels must be computed (from 0 to 1)

                Defaults to 1.
            frame_skip_ratio (int): Specifies the number of frames to be skipped from evaluation, for every evaluated frame (from 0 to 1e+06)

                Defaults to 0.
            ref_projection (int | str): projection of the reference video (from 0 to 4)

                Allowed values:
                    * e: equirectangular
                    * equirect: equirectangular
                    * c3x2: cubemap 3x2
                    * c2x3: cubemap 2x3
                    * barrel: barrel facebook's 360 format
                    * barrelsplit: barrel split facebook's 360 format

                Defaults to e.
            main_projection (int | str): projection of the main video (from 0 to 5)

                Allowed values:
                    * e: equirectangular
                    * equirect: equirectangular
                    * c3x2: cubemap 3x2
                    * c2x3: cubemap 2x3
                    * barrel: barrel facebook's 360 format
                    * barrelsplit: barrel split facebook's 360 format

                Defaults to 5.
            ref_stereo (int | str): stereo format of the reference video (from 0 to 2)

                Allowed values:
                    * mono
                    * tb
                    * lr

                Defaults to mono.
            main_stereo (int | str): stereo format of main video (from 0 to 3)

                Allowed values:
                    * mono
                    * tb
                    * lr

                Defaults to 3.
            ref_pad (float): Expansion (padding) coefficient for each cube face of the reference video (from 0 to 10)

                Defaults to 0.
            main_pad (float): Expansion (padding) coefficient for each cube face of the main video (from 0 to 10)

                Defaults to 0.
            use_tape (int): Specifies if the tape based SSIM 360 algorithm must be used independent of the input video types (from 0 to 1)

                Defaults to 0.
            heatmap_str (str): Heatmap data for view-based evaluation. For heatmap file format, please refer to EntSphericalVideoHeatmapData.

            default_heatmap_width (int): Default heatmap dimension. Will be used when dimension is not specified in heatmap data. (from 1 to 4096)

                Defaults to 32.
            default_heatmap_height (int): Default heatmap dimension. Will be used when dimension is not specified in heatmap data. (from 1 to 4096)

                Defaults to 16.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="ssim360",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
                "compute_chroma": compute_chroma,
                "frame_skip_ratio": frame_skip_ratio,
                "ref_projection": ref_projection,
                "main_projection": main_projection,
                "ref_stereo": ref_stereo,
                "main_stereo": main_stereo,
                "ref_pad": ref_pad,
                "main_pad": main_pad,
                "use_tape": use_tape,
                "heatmap_str": heatmap_str,
                "default_heatmap_width": default_heatmap_width,
                "default_heatmap_height": default_heatmap_height,
            },
        )[0]

    def stereo3d(
        self,
        in_: Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "al",
            "ar",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "irl",
            "irr",
            "icl",
            "icr",
        ]
        | int
        | None = None,
        out: Literal[
            "ab2l",
            "tb2l",
            "ab2r",
            "tb2r",
            "abl",
            "tbl",
            "abr",
            "tbr",
            "agmc",
            "agmd",
            "agmg",
            "agmh",
            "al",
            "ar",
            "arbg",
            "arcc",
            "arcd",
            "arcg",
            "arch",
            "argg",
            "aybc",
            "aybd",
            "aybg",
            "aybh",
            "irl",
            "irr",
            "ml",
            "mr",
            "sbs2l",
            "sbs2r",
            "sbsl",
            "sbsr",
            "chl",
            "chr",
            "icl",
            "icr",
            "hdmi",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Convert video stereoscopic 3D view.

        Args:
            in_ (int | str): set input format (from 16 to 32)

                Allowed values:
                    * ab2l: above below half height left first
                    * tb2l: above below half height left first
                    * ab2r: above below half height right first
                    * tb2r: above below half height right first
                    * abl: above below left first
                    * tbl: above below left first
                    * abr: above below right first
                    * tbr: above below right first
                    * al: alternating frames left first
                    * ar: alternating frames right first
                    * sbs2l: side by side half width left first
                    * sbs2r: side by side half width right first
                    * sbsl: side by side left first
                    * sbsr: side by side right first
                    * irl: interleave rows left first
                    * irr: interleave rows right first
                    * icl: interleave columns left first
                    * icr: interleave columns right first

                Defaults to sbsl.
            out (int | str): set output format (from 0 to 32)

                Allowed values:
                    * ab2l: above below half height left first
                    * tb2l: above below half height left first
                    * ab2r: above below half height right first
                    * tb2r: above below half height right first
                    * abl: above below left first
                    * tbl: above below left first
                    * abr: above below right first
                    * tbr: above below right first
                    * agmc: anaglyph green magenta color
                    * agmd: anaglyph green magenta dubois
                    * agmg: anaglyph green magenta gray
                    * agmh: anaglyph green magenta half color
                    * al: alternating frames left first
                    * ar: alternating frames right first
                    * arbg: anaglyph red blue gray
                    * arcc: anaglyph red cyan color
                    * arcd: anaglyph red cyan dubois
                    * arcg: anaglyph red cyan gray
                    * arch: anaglyph red cyan half color
                    * argg: anaglyph red green gray
                    * aybc: anaglyph yellow blue color
                    * aybd: anaglyph yellow blue dubois
                    * aybg: anaglyph yellow blue gray
                    * aybh: anaglyph yellow blue half color
                    * irl: interleave rows left first
                    * irr: interleave rows right first
                    * ml: mono left
                    * mr: mono right
                    * sbs2l: side by side half width left first
                    * sbs2r: side by side half width right first
                    * sbsl: side by side left first
                    * sbsr: side by side right first
                    * chl: checkerboard left first
                    * chr: checkerboard right first
                    * icl: interleave columns left first
                    * icr: interleave columns right first
                    * hdmi: HDMI frame pack

                Defaults to arcd.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="stereo3d",
            inputs=[self],
            named_arguments={
                "in": in_,
                "out": out,
            },
        )[0]

    def stereotools(
        self,
        level_in: float | None = None,
        level_out: float | None = None,
        balance_in: float | None = None,
        balance_out: float | None = None,
        softclip: bool | None = None,
        mutel: bool | None = None,
        muter: bool | None = None,
        phasel: bool | None = None,
        phaser: bool | None = None,
        mode: Literal[
            "lr>lr",
            "lr>ms",
            "ms>lr",
            "lr>ll",
            "lr>rr",
            "lr>l+r",
            "lr>rl",
            "ms>ll",
            "ms>rr",
            "ms>rl",
            "lr>l-r",
        ]
        | int
        | None = None,
        slev: float | None = None,
        sbal: float | None = None,
        mlev: float | None = None,
        mpan: float | None = None,
        base: float | None = None,
        delay: float | None = None,
        sclevel: float | None = None,
        phase: float | None = None,
        bmode_in: Literal["balance", "amplitude", "power"] | int | None = None,
        bmode_out: Literal["balance", "amplitude", "power"] | int | None = None,
    ) -> "Stream":
        """Apply various stereo tools.

        Args:
            level_in (float): set level in (from 0.015625 to 64)

                Defaults to 1.
            level_out (float): set level out (from 0.015625 to 64)

                Defaults to 1.
            balance_in (float): set balance in (from -1 to 1)

                Defaults to 0.
            balance_out (float): set balance out (from -1 to 1)

                Defaults to 0.
            softclip (bool): enable softclip

                Defaults to false.
            mutel (bool): mute L

                Defaults to false.
            muter (bool): mute R

                Defaults to false.
            phasel (bool): phase L

                Defaults to false.
            phaser (bool): phase R

                Defaults to false.
            mode (int | str): set stereo mode (from 0 to 10)

                Allowed values:
                    * lr>lr
                    * lr>ms
                    * ms>lr
                    * lr>ll
                    * lr>rr
                    * lr>l+r
                    * lr>rl
                    * ms>ll
                    * ms>rr
                    * ms>rl
                    * lr>l-r

                Defaults to lr>lr.
            slev (float): set side level (from 0.015625 to 64)

                Defaults to 1.
            sbal (float): set side balance (from -1 to 1)

                Defaults to 0.
            mlev (float): set middle level (from 0.015625 to 64)

                Defaults to 1.
            mpan (float): set middle pan (from -1 to 1)

                Defaults to 0.
            base (float): set stereo base (from -1 to 1)

                Defaults to 0.
            delay (float): set delay (from -20 to 20)

                Defaults to 0.
            sclevel (float): set S/C level (from 1 to 100)

                Defaults to 1.
            phase (float): set stereo phase (from 0 to 360)

                Defaults to 0.
            bmode_in (int | str): set balance in mode (from 0 to 2)

                Allowed values:
                    * balance
                    * amplitude
                    * power

                Defaults to balance.
            bmode_out (int | str): set balance out mode (from 0 to 2)

                Allowed values:
                    * balance
                    * amplitude
                    * power

                Defaults to balance.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="stereotools",
            inputs=[self],
            named_arguments={
                "level_in": level_in,
                "level_out": level_out,
                "balance_in": balance_in,
                "balance_out": balance_out,
                "softclip": softclip,
                "mutel": mutel,
                "muter": muter,
                "phasel": phasel,
                "phaser": phaser,
                "mode": mode,
                "slev": slev,
                "sbal": sbal,
                "mlev": mlev,
                "mpan": mpan,
                "base": base,
                "delay": delay,
                "sclevel": sclevel,
                "phase": phase,
                "bmode_in": bmode_in,
                "bmode_out": bmode_out,
            },
        )[0]

    def stereowiden(
        self,
        delay: float | None = None,
        feedback: float | None = None,
        crossfeed: float | None = None,
        drymix: float | None = None,
    ) -> "Stream":
        """Apply stereo widening effect.

        Args:
            delay (float): set delay time (from 1 to 100)

                Defaults to 20.
            feedback (float): set feedback gain (from 0 to 0.9)

                Defaults to 0.3.
            crossfeed (float): set cross feed (from 0 to 0.8)

                Defaults to 0.3.
            drymix (float): set dry-mix (from 0 to 1)

                Defaults to 0.8.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="stereowiden",
            inputs=[self],
            named_arguments={
                "delay": delay,
                "feedback": feedback,
                "crossfeed": crossfeed,
                "drymix": drymix,
            },
        )[0]

    def streamselect(
        self, *streams: "Stream", inputs: int | None = None, map: str | None = None
    ) -> "FilterMultiOutput":
        """Select video streams

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): number of input streams (from 2 to INT_MAX)

                Defaults to 2.
            map (str): input indexes to remap to outputs


        Returns:
            "FilterMultiOutput": A FilterMultiOutput object to access dynamic outputs.
        """
        return self._apply_dynamic_outputs_filter(
            filter_name="streamselect",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "map": map,
            },
        )

    def subtitles(
        self,
        filename: str | None = None,
        f: str | None = None,
        original_size: str | None = None,
        fontsdir: str | None = None,
        alpha: bool | None = None,
        charenc: str | None = None,
        stream_index: int | None = None,
        si: int | None = None,
        force_style: str | None = None,
        wrap_unicode: bool | None = None,
    ) -> "Stream":
        """Render text subtitles onto input video using the libass library.

        Args:
            filename (str): set the filename of file to read

            f (str): set the filename of file to read

            original_size (str): set the size of the original video (used to scale fonts)

            fontsdir (str): set the directory containing the fonts to read

            alpha (bool): enable processing of alpha channel

                Defaults to false.
            charenc (str): set input character encoding

            stream_index (int): set stream index (from -1 to INT_MAX)

                Defaults to -1.
            si (int): set stream index (from -1 to INT_MAX)

                Defaults to -1.
            force_style (str): force subtitle style

            wrap_unicode (bool): break lines according to the Unicode Line Breaking Algorithm

                Defaults to auto.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="subtitles",
            inputs=[self],
            named_arguments={
                "filename": filename,
                "f": f,
                "original_size": original_size,
                "fontsdir": fontsdir,
                "alpha": alpha,
                "charenc": charenc,
                "stream_index": stream_index,
                "si": si,
                "force_style": force_style,
                "wrap_unicode": wrap_unicode,
            },
        )[0]

    def super2xsai(
        self,
    ) -> "Stream":
        """Scale the input by 2x using the Super2xSaI pixel art algorithm.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="super2xsai", inputs=[self], named_arguments={}
        )[0]

    def superequalizer(
        self,
        _1b: float | None = None,
        _2b: float | None = None,
        _3b: float | None = None,
        _4b: float | None = None,
        _5b: float | None = None,
        _6b: float | None = None,
        _7b: float | None = None,
        _8b: float | None = None,
        _9b: float | None = None,
        _10b: float | None = None,
        _11b: float | None = None,
        _12b: float | None = None,
        _13b: float | None = None,
        _14b: float | None = None,
        _15b: float | None = None,
        _16b: float | None = None,
        _17b: float | None = None,
        _18b: float | None = None,
    ) -> "Stream":
        """Apply 18 band equalization filter.

        Args:
            _1b (float): set 65Hz band gain (from 0 to 20)

                Defaults to 1.
            _2b (float): set 92Hz band gain (from 0 to 20)

                Defaults to 1.
            _3b (float): set 131Hz band gain (from 0 to 20)

                Defaults to 1.
            _4b (float): set 185Hz band gain (from 0 to 20)

                Defaults to 1.
            _5b (float): set 262Hz band gain (from 0 to 20)

                Defaults to 1.
            _6b (float): set 370Hz band gain (from 0 to 20)

                Defaults to 1.
            _7b (float): set 523Hz band gain (from 0 to 20)

                Defaults to 1.
            _8b (float): set 740Hz band gain (from 0 to 20)

                Defaults to 1.
            _9b (float): set 1047Hz band gain (from 0 to 20)

                Defaults to 1.
            _10b (float): set 1480Hz band gain (from 0 to 20)

                Defaults to 1.
            _11b (float): set 2093Hz band gain (from 0 to 20)

                Defaults to 1.
            _12b (float): set 2960Hz band gain (from 0 to 20)

                Defaults to 1.
            _13b (float): set 4186Hz band gain (from 0 to 20)

                Defaults to 1.
            _14b (float): set 5920Hz band gain (from 0 to 20)

                Defaults to 1.
            _15b (float): set 8372Hz band gain (from 0 to 20)

                Defaults to 1.
            _16b (float): set 11840Hz band gain (from 0 to 20)

                Defaults to 1.
            _17b (float): set 16744Hz band gain (from 0 to 20)

                Defaults to 1.
            _18b (float): set 20000Hz band gain (from 0 to 20)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="superequalizer",
            inputs=[self],
            named_arguments={
                "1b": _1b,
                "2b": _2b,
                "3b": _3b,
                "4b": _4b,
                "5b": _5b,
                "6b": _6b,
                "7b": _7b,
                "8b": _8b,
                "9b": _9b,
                "10b": _10b,
                "11b": _11b,
                "12b": _12b,
                "13b": _13b,
                "14b": _14b,
                "15b": _15b,
                "16b": _16b,
                "17b": _17b,
                "18b": _18b,
            },
        )[0]

    def surround(
        self,
        chl_out: str | None = None,
        chl_in: str | None = None,
        level_in: float | None = None,
        level_out: float | None = None,
        lfe: bool | None = None,
        lfe_low: int | None = None,
        lfe_high: int | None = None,
        lfe_mode: Literal["add", "sub"] | int | None = None,
        smooth: float | None = None,
        angle: float | None = None,
        focus: float | None = None,
        fc_in: float | None = None,
        fc_out: float | None = None,
        fl_in: float | None = None,
        fl_out: float | None = None,
        fr_in: float | None = None,
        fr_out: float | None = None,
        sl_in: float | None = None,
        sl_out: float | None = None,
        sr_in: float | None = None,
        sr_out: float | None = None,
        bl_in: float | None = None,
        bl_out: float | None = None,
        br_in: float | None = None,
        br_out: float | None = None,
        bc_in: float | None = None,
        bc_out: float | None = None,
        lfe_in: float | None = None,
        lfe_out: float | None = None,
        allx: float | None = None,
        ally: float | None = None,
        fcx: float | None = None,
        flx: float | None = None,
        frx: float | None = None,
        blx: float | None = None,
        brx: float | None = None,
        slx: float | None = None,
        srx: float | None = None,
        bcx: float | None = None,
        fcy: float | None = None,
        fly: float | None = None,
        fry: float | None = None,
        bly: float | None = None,
        bry: float | None = None,
        sly: float | None = None,
        sry: float | None = None,
        bcy: float | None = None,
        win_size: int | None = None,
        win_func: Literal[
            "rect",
            "bartlett",
            "hann",
            "hanning",
            "hamming",
            "blackman",
            "welch",
            "flattop",
            "bharris",
            "bnuttall",
            "bhann",
            "sine",
            "nuttall",
            "lanczos",
            "gauss",
            "tukey",
            "dolph",
            "cauchy",
            "parzen",
            "poisson",
            "bohman",
            "kaiser",
        ]
        | int
        | None = None,
        overlap: float | None = None,
    ) -> "Stream":
        """Apply audio surround upmix filter.

        Args:
            chl_out (str): set output channel layout

                Defaults to 5.1.
            chl_in (str): set input channel layout

                Defaults to stereo.
            level_in (float): set input level (from 0 to 10)

                Defaults to 1.
            level_out (float): set output level (from 0 to 10)

                Defaults to 1.
            lfe (bool): output LFE

                Defaults to true.
            lfe_low (int): LFE low cut off (from 0 to 256)

                Defaults to 128.
            lfe_high (int): LFE high cut off (from 0 to 512)

                Defaults to 256.
            lfe_mode (int | str): set LFE channel mode (from 0 to 1)

                Allowed values:
                    * add: just add LFE channel
                    * sub: subtract LFE channel with others

                Defaults to add.
            smooth (float): set temporal smoothness strength (from 0 to 1)

                Defaults to 0.
            angle (float): set soundfield transform angle (from 0 to 360)

                Defaults to 90.
            focus (float): set soundfield transform focus (from -1 to 1)

                Defaults to 0.
            fc_in (float): set front center channel input level (from 0 to 10)

                Defaults to 1.
            fc_out (float): set front center channel output level (from 0 to 10)

                Defaults to 1.
            fl_in (float): set front left channel input level (from 0 to 10)

                Defaults to 1.
            fl_out (float): set front left channel output level (from 0 to 10)

                Defaults to 1.
            fr_in (float): set front right channel input level (from 0 to 10)

                Defaults to 1.
            fr_out (float): set front right channel output level (from 0 to 10)

                Defaults to 1.
            sl_in (float): set side left channel input level (from 0 to 10)

                Defaults to 1.
            sl_out (float): set side left channel output level (from 0 to 10)

                Defaults to 1.
            sr_in (float): set side right channel input level (from 0 to 10)

                Defaults to 1.
            sr_out (float): set side right channel output level (from 0 to 10)

                Defaults to 1.
            bl_in (float): set back left channel input level (from 0 to 10)

                Defaults to 1.
            bl_out (float): set back left channel output level (from 0 to 10)

                Defaults to 1.
            br_in (float): set back right channel input level (from 0 to 10)

                Defaults to 1.
            br_out (float): set back right channel output level (from 0 to 10)

                Defaults to 1.
            bc_in (float): set back center channel input level (from 0 to 10)

                Defaults to 1.
            bc_out (float): set back center channel output level (from 0 to 10)

                Defaults to 1.
            lfe_in (float): set lfe channel input level (from 0 to 10)

                Defaults to 1.
            lfe_out (float): set lfe channel output level (from 0 to 10)

                Defaults to 1.
            allx (float): set all channel's x spread (from -1 to 15)

                Defaults to -1.
            ally (float): set all channel's y spread (from -1 to 15)

                Defaults to -1.
            fcx (float): set front center channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            flx (float): set front left channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            frx (float): set front right channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            blx (float): set back left channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            brx (float): set back right channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            slx (float): set side left channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            srx (float): set side right channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            bcx (float): set back center channel x spread (from 0.06 to 15)

                Defaults to 0.5.
            fcy (float): set front center channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            fly (float): set front left channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            fry (float): set front right channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            bly (float): set back left channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            bry (float): set back right channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            sly (float): set side left channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            sry (float): set side right channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            bcy (float): set back center channel y spread (from 0.06 to 15)

                Defaults to 0.5.
            win_size (int): set window size (from 1024 to 65536)

                Defaults to 4096.
            win_func (int | str): set window function (from 0 to 20)

                Allowed values:
                    * rect: Rectangular
                    * bartlett: Bartlett
                    * hann: Hann
                    * hanning: Hanning
                    * hamming: Hamming
                    * blackman: Blackman
                    * welch: Welch
                    * flattop: Flat-top
                    * bharris: Blackman-Harris
                    * bnuttall: Blackman-Nuttall
                    * bhann: Bartlett-Hann
                    * sine: Sine
                    * nuttall: Nuttall
                    * lanczos: Lanczos
                    * gauss: Gauss
                    * tukey: Tukey
                    * dolph: Dolph-Chebyshev
                    * cauchy: Cauchy
                    * parzen: Parzen
                    * poisson: Poisson
                    * bohman: Bohman
                    * kaiser: Kaiser

                Defaults to hann.
            overlap (float): set window overlap (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="surround",
            inputs=[self],
            named_arguments={
                "chl_out": chl_out,
                "chl_in": chl_in,
                "level_in": level_in,
                "level_out": level_out,
                "lfe": lfe,
                "lfe_low": lfe_low,
                "lfe_high": lfe_high,
                "lfe_mode": lfe_mode,
                "smooth": smooth,
                "angle": angle,
                "focus": focus,
                "fc_in": fc_in,
                "fc_out": fc_out,
                "fl_in": fl_in,
                "fl_out": fl_out,
                "fr_in": fr_in,
                "fr_out": fr_out,
                "sl_in": sl_in,
                "sl_out": sl_out,
                "sr_in": sr_in,
                "sr_out": sr_out,
                "bl_in": bl_in,
                "bl_out": bl_out,
                "br_in": br_in,
                "br_out": br_out,
                "bc_in": bc_in,
                "bc_out": bc_out,
                "lfe_in": lfe_in,
                "lfe_out": lfe_out,
                "allx": allx,
                "ally": ally,
                "fcx": fcx,
                "flx": flx,
                "frx": frx,
                "blx": blx,
                "brx": brx,
                "slx": slx,
                "srx": srx,
                "bcx": bcx,
                "fcy": fcy,
                "fly": fly,
                "fry": fry,
                "bly": bly,
                "bry": bry,
                "sly": sly,
                "sry": sry,
                "bcy": bcy,
                "win_size": win_size,
                "win_func": win_func,
                "overlap": overlap,
            },
        )[0]

    def swaprect(
        self,
        w: str | None = None,
        h: str | None = None,
        x1: str | None = None,
        y1: str | None = None,
        x2: str | None = None,
        y2: str | None = None,
    ) -> "Stream":
        """Swap 2 rectangular objects in video.

        Args:
            w (str): set rect width

                Defaults to w/2.
            h (str): set rect height

                Defaults to h/2.
            x1 (str): set 1st rect x top left coordinate

                Defaults to w/2.
            y1 (str): set 1st rect y top left coordinate

                Defaults to h/2.
            x2 (str): set 2nd rect x top left coordinate

                Defaults to 0.
            y2 (str): set 2nd rect y top left coordinate

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="swaprect",
            inputs=[self],
            named_arguments={
                "w": w,
                "h": h,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
            },
        )[0]

    def swapuv(
        self,
    ) -> "Stream":
        """Swap U and V components.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="swapuv", inputs=[self], named_arguments={}
        )[0]

    def tblend(
        self,
        c0_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c1_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c2_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c3_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        all_mode: Literal[
            "addition",
            "addition128",
            "grainmerge",
            "and",
            "average",
            "burn",
            "darken",
            "difference",
            "difference128",
            "grainextract",
            "divide",
            "dodge",
            "exclusion",
            "extremity",
            "freeze",
            "glow",
            "hardlight",
            "hardmix",
            "heat",
            "lighten",
            "linearlight",
            "multiply",
            "multiply128",
            "negation",
            "normal",
            "or",
            "overlay",
            "phoenix",
            "pinlight",
            "reflect",
            "screen",
            "softlight",
            "subtract",
            "vividlight",
            "xor",
            "softdifference",
            "geometric",
            "harmonic",
            "bleach",
            "stain",
            "interpolate",
            "hardoverlay",
        ]
        | int
        | None = None,
        c0_expr: str | None = None,
        c1_expr: str | None = None,
        c2_expr: str | None = None,
        c3_expr: str | None = None,
        all_expr: str | None = None,
        c0_opacity: float | None = None,
        c1_opacity: float | None = None,
        c2_opacity: float | None = None,
        c3_opacity: float | None = None,
        all_opacity: float | None = None,
    ) -> "Stream":
        """Blend successive frames.

        Args:
            c0_mode (int | str): set component #0 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c1_mode (int | str): set component #1 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c2_mode (int | str): set component #2 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            c3_mode (int | str): set component #3 blend mode (from 0 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to normal.
            all_mode (int | str): set blend mode for all components (from -1 to 39)

                Allowed values:
                    * addition
                    * addition128
                    * grainmerge
                    * and
                    * average
                    * burn
                    * darken
                    * difference
                    * difference128
                    * grainextract
                    * divide
                    * dodge
                    * exclusion
                    * extremity
                    * freeze
                    * glow
                    * hardlight
                    * hardmix
                    * heat
                    * lighten
                    * linearlight
                    * multiply
                    * multiply128
                    * negation
                    * normal
                    * or
                    * overlay
                    * phoenix
                    * pinlight
                    * reflect
                    * screen
                    * softlight
                    * subtract
                    * vividlight
                    * xor
                    * softdifference
                    * geometric
                    * harmonic
                    * bleach
                    * stain
                    * interpolate
                    * hardoverlay

                Defaults to -1.
            c0_expr (str): set color component #0 expression

            c1_expr (str): set color component #1 expression

            c2_expr (str): set color component #2 expression

            c3_expr (str): set color component #3 expression

            all_expr (str): set expression for all color components

            c0_opacity (float): set color component #0 opacity (from 0 to 1)

                Defaults to 1.
            c1_opacity (float): set color component #1 opacity (from 0 to 1)

                Defaults to 1.
            c2_opacity (float): set color component #2 opacity (from 0 to 1)

                Defaults to 1.
            c3_opacity (float): set color component #3 opacity (from 0 to 1)

                Defaults to 1.
            all_opacity (float): set opacity for all color components (from 0 to 1)

                Defaults to 1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tblend",
            inputs=[self],
            named_arguments={
                "c0_mode": c0_mode,
                "c1_mode": c1_mode,
                "c2_mode": c2_mode,
                "c3_mode": c3_mode,
                "all_mode": all_mode,
                "c0_expr": c0_expr,
                "c1_expr": c1_expr,
                "c2_expr": c2_expr,
                "c3_expr": c3_expr,
                "all_expr": all_expr,
                "c0_opacity": c0_opacity,
                "c1_opacity": c1_opacity,
                "c2_opacity": c2_opacity,
                "c3_opacity": c3_opacity,
                "all_opacity": all_opacity,
            },
        )[0]

    def telecine(
        self,
        first_field: Literal["top", "t", "bottom", "b"] | int | None = None,
        pattern: str | None = None,
    ) -> "Stream":
        """Apply a telecine pattern.

        Args:
            first_field (int | str): select first field (from 0 to 1)

                Allowed values:
                    * top: select top field first
                    * t: select top field first
                    * bottom: select bottom field first
                    * b: select bottom field first

                Defaults to top.
            pattern (str): pattern that describe for how many fields a frame is to be displayed

                Defaults to 23.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="telecine",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
                "pattern": pattern,
            },
        )[0]

    def thistogram(
        self,
        width: int | None = None,
        w: int | None = None,
        display_mode: Literal["overlay", "parade", "stack"] | int | None = None,
        d: Literal["overlay", "parade", "stack"] | int | None = None,
        levels_mode: Literal["linear", "logarithmic"] | int | None = None,
        m: Literal["linear", "logarithmic"] | int | None = None,
        components: int | None = None,
        c: int | None = None,
        bgopacity: float | None = None,
        b: float | None = None,
        envelope: bool | None = None,
        e: bool | None = None,
        ecolor: str | None = None,
        ec: str | None = None,
        slide: Literal["frame", "replace", "scroll", "rscroll", "picture"]
        | int
        | None = None,
    ) -> "Stream":
        """Compute and draw a temporal histogram.

        Args:
            width (int): set width (from 0 to 8192)

                Defaults to 0.
            w (int): set width (from 0 to 8192)

                Defaults to 0.
            display_mode (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * parade
                    * stack

                Defaults to stack.
            d (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * parade
                    * stack

                Defaults to stack.
            levels_mode (int | str): set levels mode (from 0 to 1)

                Allowed values:
                    * linear
                    * logarithmic

                Defaults to linear.
            m (int | str): set levels mode (from 0 to 1)

                Allowed values:
                    * linear
                    * logarithmic

                Defaults to linear.
            components (int): set color components to display (from 1 to 15)

                Defaults to 7.
            c (int): set color components to display (from 1 to 15)

                Defaults to 7.
            bgopacity (float): set background opacity (from 0 to 1)

                Defaults to 0.9.
            b (float): set background opacity (from 0 to 1)

                Defaults to 0.9.
            envelope (bool): display envelope

                Defaults to false.
            e (bool): display envelope

                Defaults to false.
            ecolor (str): set envelope color

                Defaults to gold.
            ec (str): set envelope color

                Defaults to gold.
            slide (int | str): set slide mode (from 0 to 4)

                Allowed values:
                    * frame: draw new frames
                    * replace: replace old columns with new
                    * scroll: scroll from right to left
                    * rscroll: scroll from left to right
                    * picture: display graph in single frame

                Defaults to replace.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="thistogram",
            inputs=[self],
            named_arguments={
                "width": width,
                "w": w,
                "display_mode": display_mode,
                "d": d,
                "levels_mode": levels_mode,
                "m": m,
                "components": components,
                "c": c,
                "bgopacity": bgopacity,
                "b": b,
                "envelope": envelope,
                "e": e,
                "ecolor": ecolor,
                "ec": ec,
                "slide": slide,
            },
        )[0]

    def threshold(
        self,
        threshold_stream: "Stream",
        min_stream: "Stream",
        max_stream: "Stream",
        planes: int | None = None,
    ) -> "Stream":
        """Threshold first video stream using other video streams.

        Args:
            threshold_stream (Stream): Input video stream.
            min_stream (Stream): Input video stream.
            max_stream (Stream): Input video stream.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="threshold",
            inputs=[self, threshold_stream, min_stream, max_stream],
            named_arguments={
                "planes": planes,
            },
        )[0]

    def thumbnail(
        self,
        n: int | None = None,
        log: Literal["quiet", "info", "verbose"] | int | None = None,
    ) -> "Stream":
        """Select the most representative frame in a given sequence of consecutive frames.

        Args:
            n (int): set the frames batch size (from 2 to INT_MAX)

                Defaults to 100.
            log (int | str): force stats logging level (from INT_MIN to INT_MAX)

                Allowed values:
                    * quiet: logging disabled
                    * info: information logging level
                    * verbose: verbose logging level

                Defaults to info.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="thumbnail",
            inputs=[self],
            named_arguments={
                "n": n,
                "log": log,
            },
        )[0]

    def tile(
        self,
        layout: str | None = None,
        nb_frames: int | None = None,
        margin: int | None = None,
        padding: int | None = None,
        color: str | None = None,
        overlap: int | None = None,
        init_padding: int | None = None,
    ) -> "Stream":
        """Tile several successive frames together.

        Args:
            layout (str): set grid size

                Defaults to 6x5.
            nb_frames (int): set maximum number of frame to render (from 0 to INT_MAX)

                Defaults to 0.
            margin (int): set outer border margin in pixels (from 0 to 1024)

                Defaults to 0.
            padding (int): set inner border thickness in pixels (from 0 to 1024)

                Defaults to 0.
            color (str): set the color of the unused area

                Defaults to black.
            overlap (int): set how many frames to overlap for each render (from 0 to INT_MAX)

                Defaults to 0.
            init_padding (int): set how many frames to initially pad (from 0 to INT_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tile",
            inputs=[self],
            named_arguments={
                "layout": layout,
                "nb_frames": nb_frames,
                "margin": margin,
                "padding": padding,
                "color": color,
                "overlap": overlap,
                "init_padding": init_padding,
            },
        )[0]

    def tiltandshift(
        self,
        _tilt: int | None = None,
        _start: Literal["none", "frame", "black"] | int | None = None,
        _end: Literal["none", "frame", "black"] | int | None = None,
        _hold: int | None = None,
        _pad: int | None = None,
    ) -> "Stream":
        """Generate a tilt-and-shift'd video.

        Args:
            _tilt (int): Tilt the video horizontally while shifting (from 0 to 1)

                Defaults to 1.
            _start (int | str): Action at the start of input (from 0 to 3)

                Allowed values:
                    * none: Start immediately (default)
                    * frame: Use the first frames
                    * black: Fill with black

                Defaults to none.
            _end (int | str): Action at the end of input (from 0 to 3)

                Allowed values:
                    * none: Do not pad at the end (default)
                    * frame: Use the last frame
                    * black: Fill with black

                Defaults to none.
            _hold (int): Number of columns to hold at the start of the video (from 0 to INT_MAX)

                Defaults to 0.
            _pad (int): Number of columns to pad at the end of the video (from 0 to INT_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tiltandshift",
            inputs=[self],
            named_arguments={
                "-tilt": _tilt,
                "-start": _start,
                "-end": _end,
                "-hold": _hold,
                "-pad": _pad,
            },
        )[0]

    def tiltshelf(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Apply a tilt shelf filter.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tiltshelf",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def tinterlace(
        self,
        mode: Literal[
            "merge",
            "drop_even",
            "drop_odd",
            "pad",
            "interleave_top",
            "interleave_bottom",
            "interlacex2",
            "mergex2",
        ]
        | int
        | None = None,
    ) -> "Stream":
        """Perform temporal field interlacing.

        Args:
            mode (int | str): select interlace mode (from 0 to 7)

                Allowed values:
                    * merge: merge fields
                    * drop_even: drop even fields
                    * drop_odd: drop odd fields
                    * pad: pad alternate lines with black
                    * interleave_top: interleave top and bottom fields
                    * interleave_bottom: interleave bottom and top fields
                    * interlacex2: interlace fields from two consecutive frames
                    * mergex2: merge fields keeping same frame rate

                Defaults to merge.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tinterlace",
            inputs=[self],
            named_arguments={
                "mode": mode,
            },
        )[0]

    def tlut2(
        self,
        c0: str | None = None,
        c1: str | None = None,
        c2: str | None = None,
        c3: str | None = None,
    ) -> "Stream":
        """Compute and apply a lookup table from two successive frames.

        Args:
            c0 (str): set component #0 expression

                Defaults to x.
            c1 (str): set component #1 expression

                Defaults to x.
            c2 (str): set component #2 expression

                Defaults to x.
            c3 (str): set component #3 expression

                Defaults to x.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tlut2",
            inputs=[self],
            named_arguments={
                "c0": c0,
                "c1": c1,
                "c2": c2,
                "c3": c3,
            },
        )[0]

    def tmedian(
        self,
        radius: int | None = None,
        planes: int | None = None,
        percentile: float | None = None,
    ) -> "Stream":
        """Pick median pixels from successive frames.

        Args:
            radius (int): set median filter radius (from 1 to 127)

                Defaults to 1.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            percentile (float): set percentile (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tmedian",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "planes": planes,
                "percentile": percentile,
            },
        )[0]

    def tmidequalizer(
        self,
        radius: int | None = None,
        sigma: float | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply Temporal Midway Equalization.

        Args:
            radius (int): set radius (from 1 to 127)

                Defaults to 5.
            sigma (float): set sigma (from 0 to 1)

                Defaults to 0.5.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tmidequalizer",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "sigma": sigma,
                "planes": planes,
            },
        )[0]

    def tmix(
        self,
        frames: int | None = None,
        weights: str | None = None,
        scale: float | None = None,
        planes: str | None = None,
    ) -> "Stream":
        """Mix successive video frames.

        Args:
            frames (int): set number of successive frames to mix (from 1 to 1024)

                Defaults to 3.
            weights (str): set weight for each frame

                Defaults to 1 1 1.
            scale (float): set scale (from 0 to 32767)

                Defaults to 0.
            planes (str): set what planes to filter

                Defaults to F.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tmix",
            inputs=[self],
            named_arguments={
                "frames": frames,
                "weights": weights,
                "scale": scale,
                "planes": planes,
            },
        )[0]

    def tonemap(
        self,
        tonemap: Literal[
            "none", "linear", "gamma", "clip", "reinhard", "hable", "mobius"
        ]
        | int
        | None = None,
        param: float | None = None,
        desat: float | None = None,
        peak: float | None = None,
    ) -> "Stream":
        """Conversion to/from different dynamic ranges.

        Args:
            tonemap (int | str): tonemap algorithm selection (from 0 to 6)

                Allowed values:
                    * none
                    * linear
                    * gamma
                    * clip
                    * reinhard
                    * hable
                    * mobius

                Defaults to none.
            param (float): tonemap parameter (from DBL_MIN to DBL_MAX)

                Defaults to nan.
            desat (float): desaturation strength (from 0 to DBL_MAX)

                Defaults to 2.
            peak (float): signal peak override (from 0 to DBL_MAX)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tonemap",
            inputs=[self],
            named_arguments={
                "tonemap": tonemap,
                "param": param,
                "desat": desat,
                "peak": peak,
            },
        )[0]

    def tpad(
        self,
        start: int | None = None,
        stop: int | None = None,
        start_mode: Literal["add", "clone"] | int | None = None,
        stop_mode: Literal["add", "clone"] | int | None = None,
        start_duration: str | None = None,
        stop_duration: str | None = None,
        color: str | None = None,
    ) -> "Stream":
        """Temporarily pad video frames.

        Args:
            start (int): set the number of frames to delay input (from 0 to INT_MAX)

                Defaults to 0.
            stop (int): set the number of frames to add after input finished (from -1 to INT_MAX)

                Defaults to 0.
            start_mode (int | str): set the mode of added frames to start (from 0 to 1)

                Allowed values:
                    * add: add solid-color frames
                    * clone: clone first/last frame

                Defaults to add.
            stop_mode (int | str): set the mode of added frames to end (from 0 to 1)

                Allowed values:
                    * add: add solid-color frames
                    * clone: clone first/last frame

                Defaults to add.
            start_duration (str): set the duration to delay input

                Defaults to 0.
            stop_duration (str): set the duration to pad input

                Defaults to 0.
            color (str): set the color of the added frames

                Defaults to black.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tpad",
            inputs=[self],
            named_arguments={
                "start": start,
                "stop": stop,
                "start_mode": start_mode,
                "stop_mode": stop_mode,
                "start_duration": start_duration,
                "stop_duration": stop_duration,
                "color": color,
            },
        )[0]

    def transpose(
        self,
        dir: Literal["cclock_flip", "clock", "cclock", "clock_flip"]
        | int
        | None = None,
        passthrough: Literal["none", "portrait", "landscape"] | int | None = None,
    ) -> "Stream":
        """Transpose input video.

        Args:
            dir (int | str): set transpose direction (from 0 to 7)

                Allowed values:
                    * cclock_flip: rotate counter-clockwise with vertical flip
                    * clock: rotate clockwise
                    * cclock: rotate counter-clockwise
                    * clock_flip: rotate clockwise with vertical flip

                Defaults to cclock_flip.
            passthrough (int | str): do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX)

                Allowed values:
                    * none: always apply transposition
                    * portrait: preserve portrait geometry
                    * landscape: preserve landscape geometry

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="transpose",
            inputs=[self],
            named_arguments={
                "dir": dir,
                "passthrough": passthrough,
            },
        )[0]

    def transpose_vt(
        self,
        dir: Literal[
            "cclock_flip", "clock", "cclock", "clock_flip", "reversal", "hflip", "vflip"
        ]
        | int
        | None = None,
        passthrough: Literal["none", "portrait", "landscape"] | int | None = None,
    ) -> "Stream":
        """Transpose Videotoolbox frames

        Args:
            dir (int | str): set transpose direction (from 0 to 6)

                Allowed values:
                    * cclock_flip: rotate counter-clockwise with vertical flip
                    * clock: rotate clockwise
                    * cclock: rotate counter-clockwise
                    * clock_flip: rotate clockwise with vertical flip
                    * reversal: rotate by half-turn
                    * hflip: flip horizontally
                    * vflip: flip vertically

                Defaults to cclock_flip.
            passthrough (int | str): do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX)

                Allowed values:
                    * none: always apply transposition
                    * portrait: preserve portrait geometry
                    * landscape: preserve landscape geometry

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="transpose_vt",
            inputs=[self],
            named_arguments={
                "dir": dir,
                "passthrough": passthrough,
            },
        )[0]

    def treble(
        self,
        frequency: float | None = None,
        f: float | None = None,
        width_type: Literal["h", "q", "o", "s", "k"] | int | None = None,
        t: Literal["h", "q", "o", "s", "k"] | int | None = None,
        width: float | None = None,
        w: float | None = None,
        gain: float | None = None,
        g: float | None = None,
        poles: int | None = None,
        p: int | None = None,
        mix: float | None = None,
        m: float | None = None,
        channels: str | None = None,
        c: str | None = None,
        normalize: bool | None = None,
        n: bool | None = None,
        transform: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        a: Literal["di", "dii", "tdi", "tdii", "latt", "svf", "zdf"]
        | int
        | None = None,
        precision: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        r: Literal["auto", "s16", "s32", "f32", "f64"] | int | None = None,
        blocksize: int | None = None,
        b: int | None = None,
    ) -> "Stream":
        """Boost or cut upper frequencies.

        Args:
            frequency (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            f (float): set central frequency (from 0 to 999999)

                Defaults to 3000.
            width_type (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            t (int | str): set filter-width type (from 1 to 5)

                Allowed values:
                    * h: Hz
                    * q: Q-Factor
                    * o: octave
                    * s: slope
                    * k: kHz

                Defaults to q.
            width (float): set width (from 0 to 99999)

                Defaults to 0.5.
            w (float): set width (from 0 to 99999)

                Defaults to 0.5.
            gain (float): set gain (from -900 to 900)

                Defaults to 0.
            g (float): set gain (from -900 to 900)

                Defaults to 0.
            poles (int): set number of poles (from 1 to 2)

                Defaults to 2.
            p (int): set number of poles (from 1 to 2)

                Defaults to 2.
            mix (float): set mix (from 0 to 1)

                Defaults to 1.
            m (float): set mix (from 0 to 1)

                Defaults to 1.
            channels (str): set channels to filter

                Defaults to all.
            c (str): set channels to filter

                Defaults to all.
            normalize (bool): normalize coefficients

                Defaults to false.
            n (bool): normalize coefficients

                Defaults to false.
            transform (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            a (int | str): set transform type (from 0 to 6)

                Allowed values:
                    * di: direct form I
                    * dii: direct form II
                    * tdi: transposed direct form I
                    * tdii: transposed direct form II
                    * latt: lattice-ladder form
                    * svf: state variable filter form
                    * zdf: zero-delay filter form

                Defaults to di.
            precision (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            r (int | str): set filtering precision (from -1 to 3)

                Allowed values:
                    * auto: automatic
                    * s16: signed 16-bit
                    * s32: signed 32-bit
                    * f32: floating-point single
                    * f64: floating-point double

                Defaults to auto.
            blocksize (int): set the block size (from 0 to 32768)

                Defaults to 0.
            b (int): set the block size (from 0 to 32768)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="treble",
            inputs=[self],
            named_arguments={
                "frequency": frequency,
                "f": f,
                "width_type": width_type,
                "t": t,
                "width": width,
                "w": w,
                "gain": gain,
                "g": g,
                "poles": poles,
                "p": p,
                "mix": mix,
                "m": m,
                "channels": channels,
                "c": c,
                "normalize": normalize,
                "n": n,
                "transform": transform,
                "a": a,
                "precision": precision,
                "r": r,
                "blocksize": blocksize,
                "b": b,
            },
        )[0]

    def tremolo(self, f: float | None = None, d: float | None = None) -> "Stream":
        """Apply tremolo effect.

        Args:
            f (float): set frequency in hertz (from 0.1 to 20000)

                Defaults to 5.
            d (float): set depth as percentage (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="tremolo",
            inputs=[self],
            named_arguments={
                "f": f,
                "d": d,
            },
        )[0]

    def trim(
        self,
        start: str | None = None,
        starti: str | None = None,
        end: str | None = None,
        endi: str | None = None,
        start_pts: str | None = None,
        end_pts: str | None = None,
        duration: str | None = None,
        durationi: str | None = None,
        start_frame: str | None = None,
        end_frame: str | None = None,
    ) -> "Stream":
        """Pick one continuous section from the input, drop the rest.

        Args:
            start (str): Timestamp of the first frame that should be passed

                Defaults to INT64_MAX.
            starti (str): Timestamp of the first frame that should be passed

                Defaults to INT64_MAX.
            end (str): Timestamp of the first frame that should be dropped again

                Defaults to INT64_MAX.
            endi (str): Timestamp of the first frame that should be dropped again

                Defaults to INT64_MAX.
            start_pts (str): Timestamp of the first frame that should be  passed (from I64_MIN to I64_MAX)

                Defaults to I64_MIN.
            end_pts (str): Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX)

                Defaults to I64_MIN.
            duration (str): Maximum duration of the output

                Defaults to 0.
            durationi (str): Maximum duration of the output

                Defaults to 0.
            start_frame (str): Number of the first frame that should be passed to the output (from -1 to I64_MAX)

                Defaults to -1.
            end_frame (str): Number of the first frame that should be dropped again (from 0 to I64_MAX)

                Defaults to I64_MAX.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="trim",
            inputs=[self],
            named_arguments={
                "start": start,
                "starti": starti,
                "end": end,
                "endi": endi,
                "start_pts": start_pts,
                "end_pts": end_pts,
                "duration": duration,
                "durationi": durationi,
                "start_frame": start_frame,
                "end_frame": end_frame,
            },
        )[0]

    def unpremultiply(
        self, *streams: "Stream", planes: int | None = None, inplace: bool | None = None
    ) -> "Stream":
        """UnPreMultiply first stream with first plane of second stream.

        Args:
            *streams (Stream): One or more input streams.
            planes (int): set planes (from 0 to 15)

                Defaults to 15.
            inplace (bool): enable inplace mode

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="unpremultiply",
            inputs=[self, *streams],
            named_arguments={
                "planes": planes,
                "inplace": inplace,
            },
        )[0]

    def unsharp(
        self,
        luma_msize_x: int | None = None,
        lx: int | None = None,
        luma_msize_y: int | None = None,
        ly: int | None = None,
        luma_amount: float | None = None,
        la: float | None = None,
        chroma_msize_x: int | None = None,
        cx: int | None = None,
        chroma_msize_y: int | None = None,
        cy: int | None = None,
        chroma_amount: float | None = None,
        ca: float | None = None,
        alpha_msize_x: int | None = None,
        ax: int | None = None,
        alpha_msize_y: int | None = None,
        ay: int | None = None,
        alpha_amount: float | None = None,
        aa: float | None = None,
    ) -> "Stream":
        """Sharpen or blur the input video.

        Args:
            luma_msize_x (int): set luma matrix horizontal size (from 3 to 23)

                Defaults to 5.
            lx (int): set luma matrix horizontal size (from 3 to 23)

                Defaults to 5.
            luma_msize_y (int): set luma matrix vertical size (from 3 to 23)

                Defaults to 5.
            ly (int): set luma matrix vertical size (from 3 to 23)

                Defaults to 5.
            luma_amount (float): set luma effect strength (from -2 to 5)

                Defaults to 1.
            la (float): set luma effect strength (from -2 to 5)

                Defaults to 1.
            chroma_msize_x (int): set chroma matrix horizontal size (from 3 to 23)

                Defaults to 5.
            cx (int): set chroma matrix horizontal size (from 3 to 23)

                Defaults to 5.
            chroma_msize_y (int): set chroma matrix vertical size (from 3 to 23)

                Defaults to 5.
            cy (int): set chroma matrix vertical size (from 3 to 23)

                Defaults to 5.
            chroma_amount (float): set chroma effect strength (from -2 to 5)

                Defaults to 0.
            ca (float): set chroma effect strength (from -2 to 5)

                Defaults to 0.
            alpha_msize_x (int): set alpha matrix horizontal size (from 3 to 23)

                Defaults to 5.
            ax (int): set alpha matrix horizontal size (from 3 to 23)

                Defaults to 5.
            alpha_msize_y (int): set alpha matrix vertical size (from 3 to 23)

                Defaults to 5.
            ay (int): set alpha matrix vertical size (from 3 to 23)

                Defaults to 5.
            alpha_amount (float): set alpha effect strength (from -2 to 5)

                Defaults to 0.
            aa (float): set alpha effect strength (from -2 to 5)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="unsharp",
            inputs=[self],
            named_arguments={
                "luma_msize_x": luma_msize_x,
                "lx": lx,
                "luma_msize_y": luma_msize_y,
                "ly": ly,
                "luma_amount": luma_amount,
                "la": la,
                "chroma_msize_x": chroma_msize_x,
                "cx": cx,
                "chroma_msize_y": chroma_msize_y,
                "cy": cy,
                "chroma_amount": chroma_amount,
                "ca": ca,
                "alpha_msize_x": alpha_msize_x,
                "ax": ax,
                "alpha_msize_y": alpha_msize_y,
                "ay": ay,
                "alpha_amount": alpha_amount,
                "aa": aa,
            },
        )[0]

    def untile(self, layout: str | None = None) -> "Stream":
        """Untile a frame into a sequence of frames.

        Args:
            layout (str): set grid size

                Defaults to 6x5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="untile",
            inputs=[self],
            named_arguments={
                "layout": layout,
            },
        )[0]

    def uspp(
        self,
        quality: int | None = None,
        qp: int | None = None,
        use_bframe_qp: bool | None = None,
        codec: str | None = None,
    ) -> "Stream":
        """Apply Ultra Simple / Slow Post-processing filter.

        Args:
            quality (int): set quality (from 0 to 8)

                Defaults to 3.
            qp (int): force a constant quantizer parameter (from 0 to 63)

                Defaults to 0.
            use_bframe_qp (bool): use B-frames' QP

                Defaults to false.
            codec (str): Codec name

                Defaults to snow.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="uspp",
            inputs=[self],
            named_arguments={
                "quality": quality,
                "qp": qp,
                "use_bframe_qp": use_bframe_qp,
                "codec": codec,
            },
        )[0]

    def v360(
        self,
        input: Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | int
        | None = None,
        output: Literal[
            "e",
            "equirect",
            "c3x2",
            "c6x1",
            "eac",
            "dfisheye",
            "flat",
            "rectilinear",
            "gnomonic",
            "barrel",
            "fb",
            "c1x6",
            "sg",
            "mercator",
            "ball",
            "hammer",
            "sinusoidal",
            "fisheye",
            "pannini",
            "cylindrical",
            "perspective",
            "tetrahedron",
            "barrelsplit",
            "tsp",
            "hequirect",
            "he",
            "equisolid",
            "og",
            "octahedron",
            "cylindricalea",
        ]
        | int
        | None = None,
        interp: Literal[
            "near",
            "nearest",
            "line",
            "linear",
            "lagrange9",
            "cube",
            "cubic",
            "lanc",
            "lanczos",
            "sp16",
            "spline16",
            "gauss",
            "gaussian",
            "mitchell",
        ]
        | int
        | None = None,
        w: int | None = None,
        h: int | None = None,
        in_stereo: Literal["2d", "sbs", "tb"] | int | None = None,
        out_stereo: Literal["2d", "sbs", "tb"] | int | None = None,
        in_forder: str | None = None,
        out_forder: str | None = None,
        in_frot: str | None = None,
        out_frot: str | None = None,
        in_pad: float | None = None,
        out_pad: float | None = None,
        fin_pad: int | None = None,
        fout_pad: int | None = None,
        yaw: float | None = None,
        pitch: float | None = None,
        roll: float | None = None,
        rorder: str | None = None,
        h_fov: float | None = None,
        v_fov: float | None = None,
        d_fov: float | None = None,
        h_flip: bool | None = None,
        v_flip: bool | None = None,
        d_flip: bool | None = None,
        ih_flip: bool | None = None,
        iv_flip: bool | None = None,
        in_trans: bool | None = None,
        out_trans: bool | None = None,
        ih_fov: float | None = None,
        iv_fov: float | None = None,
        id_fov: float | None = None,
        h_offset: float | None = None,
        v_offset: float | None = None,
        alpha_mask: bool | None = None,
        reset_rot: bool | None = None,
    ) -> "Stream":
        """Convert 360 projection of video.

        Args:
            input (int | str): set input projection (from 0 to 24)

                Allowed values:
                    * e: equirectangular
                    * equirect: equirectangular
                    * c3x2: cubemap 3x2
                    * c6x1: cubemap 6x1
                    * eac: equi-angular cubemap
                    * dfisheye: dual fisheye
                    * flat: regular video
                    * rectilinear: regular video
                    * gnomonic: regular video
                    * barrel: barrel facebook's 360 format
                    * fb: barrel facebook's 360 format
                    * c1x6: cubemap 1x6
                    * sg: stereographic
                    * mercator: mercator
                    * ball: ball
                    * hammer: hammer
                    * sinusoidal: sinusoidal
                    * fisheye: fisheye
                    * pannini: pannini
                    * cylindrical: cylindrical
                    * tetrahedron: tetrahedron
                    * barrelsplit: barrel split facebook's 360 format
                    * tsp: truncated square pyramid
                    * hequirect: half equirectangular
                    * he: half equirectangular
                    * equisolid: equisolid
                    * og: orthographic
                    * octahedron: octahedron
                    * cylindricalea: cylindrical equal area

                Defaults to e.
            output (int | str): set output projection (from 0 to 24)

                Allowed values:
                    * e: equirectangular
                    * equirect: equirectangular
                    * c3x2: cubemap 3x2
                    * c6x1: cubemap 6x1
                    * eac: equi-angular cubemap
                    * dfisheye: dual fisheye
                    * flat: regular video
                    * rectilinear: regular video
                    * gnomonic: regular video
                    * barrel: barrel facebook's 360 format
                    * fb: barrel facebook's 360 format
                    * c1x6: cubemap 1x6
                    * sg: stereographic
                    * mercator: mercator
                    * ball: ball
                    * hammer: hammer
                    * sinusoidal: sinusoidal
                    * fisheye: fisheye
                    * pannini: pannini
                    * cylindrical: cylindrical
                    * perspective: perspective
                    * tetrahedron: tetrahedron
                    * barrelsplit: barrel split facebook's 360 format
                    * tsp: truncated square pyramid
                    * hequirect: half equirectangular
                    * he: half equirectangular
                    * equisolid: equisolid
                    * og: orthographic
                    * octahedron: octahedron
                    * cylindricalea: cylindrical equal area

                Defaults to c3x2.
            interp (int | str): set interpolation method (from 0 to 7)

                Allowed values:
                    * near: nearest neighbour
                    * nearest: nearest neighbour
                    * line: bilinear interpolation
                    * linear: bilinear interpolation
                    * lagrange9: lagrange9 interpolation
                    * cube: bicubic interpolation
                    * cubic: bicubic interpolation
                    * lanc: lanczos interpolation
                    * lanczos: lanczos interpolation
                    * sp16: spline16 interpolation
                    * spline16: spline16 interpolation
                    * gauss: gaussian interpolation
                    * gaussian: gaussian interpolation
                    * mitchell: mitchell interpolation

                Defaults to line.
            w (int): output width (from 0 to 32767)

                Defaults to 0.
            h (int): output height (from 0 to 32767)

                Defaults to 0.
            in_stereo (int | str): input stereo format (from 0 to 2)

                Allowed values:
                    * 2d: 2d mono
                    * sbs: side by side
                    * tb: top bottom

                Defaults to 2d.
            out_stereo (int | str): output stereo format (from 0 to 2)

                Allowed values:
                    * 2d: 2d mono
                    * sbs: side by side
                    * tb: top bottom

                Defaults to 2d.
            in_forder (str): input cubemap face order

                Defaults to rludfb.
            out_forder (str): output cubemap face order

                Defaults to rludfb.
            in_frot (str): input cubemap face rotation

                Defaults to 000000.
            out_frot (str): output cubemap face rotation

                Defaults to 000000.
            in_pad (float): percent input cubemap pads (from 0 to 0.1)

                Defaults to 0.
            out_pad (float): percent output cubemap pads (from 0 to 0.1)

                Defaults to 0.
            fin_pad (int): fixed input cubemap pads (from 0 to 100)

                Defaults to 0.
            fout_pad (int): fixed output cubemap pads (from 0 to 100)

                Defaults to 0.
            yaw (float): yaw rotation (from -180 to 180)

                Defaults to 0.
            pitch (float): pitch rotation (from -180 to 180)

                Defaults to 0.
            roll (float): roll rotation (from -180 to 180)

                Defaults to 0.
            rorder (str): rotation order

                Defaults to ypr.
            h_fov (float): output horizontal field of view (from 0 to 360)

                Defaults to 0.
            v_fov (float): output vertical field of view (from 0 to 360)

                Defaults to 0.
            d_fov (float): output diagonal field of view (from 0 to 360)

                Defaults to 0.
            h_flip (bool): flip out video horizontally

                Defaults to false.
            v_flip (bool): flip out video vertically

                Defaults to false.
            d_flip (bool): flip out video indepth

                Defaults to false.
            ih_flip (bool): flip in video horizontally

                Defaults to false.
            iv_flip (bool): flip in video vertically

                Defaults to false.
            in_trans (bool): transpose video input

                Defaults to false.
            out_trans (bool): transpose video output

                Defaults to false.
            ih_fov (float): input horizontal field of view (from 0 to 360)

                Defaults to 0.
            iv_fov (float): input vertical field of view (from 0 to 360)

                Defaults to 0.
            id_fov (float): input diagonal field of view (from 0 to 360)

                Defaults to 0.
            h_offset (float): output horizontal off-axis offset (from -1 to 1)

                Defaults to 0.
            v_offset (float): output vertical off-axis offset (from -1 to 1)

                Defaults to 0.
            alpha_mask (bool): build mask in alpha plane

                Defaults to false.
            reset_rot (bool): reset rotation

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="v360",
            inputs=[self],
            named_arguments={
                "input": input,
                "output": output,
                "interp": interp,
                "w": w,
                "h": h,
                "in_stereo": in_stereo,
                "out_stereo": out_stereo,
                "in_forder": in_forder,
                "out_forder": out_forder,
                "in_frot": in_frot,
                "out_frot": out_frot,
                "in_pad": in_pad,
                "out_pad": out_pad,
                "fin_pad": fin_pad,
                "fout_pad": fout_pad,
                "yaw": yaw,
                "pitch": pitch,
                "roll": roll,
                "rorder": rorder,
                "h_fov": h_fov,
                "v_fov": v_fov,
                "d_fov": d_fov,
                "h_flip": h_flip,
                "v_flip": v_flip,
                "d_flip": d_flip,
                "ih_flip": ih_flip,
                "iv_flip": iv_flip,
                "in_trans": in_trans,
                "out_trans": out_trans,
                "ih_fov": ih_fov,
                "iv_fov": iv_fov,
                "id_fov": id_fov,
                "h_offset": h_offset,
                "v_offset": v_offset,
                "alpha_mask": alpha_mask,
                "reset_rot": reset_rot,
            },
        )[0]

    def vaguedenoiser(
        self,
        threshold: float | None = None,
        method: Literal["hard", "soft", "garrote"] | int | None = None,
        nsteps: int | None = None,
        percent: float | None = None,
        planes: int | None = None,
        type: Literal["universal", "bayes"] | int | None = None,
    ) -> "Stream":
        """Apply a Wavelet based Denoiser.

        Args:
            threshold (float): set filtering strength (from 0 to DBL_MAX)

                Defaults to 2.
            method (int | str): set filtering method (from 0 to 2)

                Allowed values:
                    * hard: hard thresholding
                    * soft: soft thresholding
                    * garrote: garrote thresholding

                Defaults to garrote.
            nsteps (int): set number of steps (from 1 to 32)

                Defaults to 6.
            percent (float): set percent of full denoising (from 0 to 100)

                Defaults to 85.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            type (int | str): set threshold type (from 0 to 1)

                Allowed values:
                    * universal: universal (VisuShrink)
                    * bayes: bayes (BayesShrink)

                Defaults to universal.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vaguedenoiser",
            inputs=[self],
            named_arguments={
                "threshold": threshold,
                "method": method,
                "nsteps": nsteps,
                "percent": percent,
                "planes": planes,
                "type": type,
            },
        )[0]

    def varblur(
        self,
        radius_stream: "Stream",
        min_r: int | None = None,
        max_r: int | None = None,
        planes: int | None = None,
    ) -> "Stream":
        """Apply Variable Blur filter.

        Args:
            radius_stream (Stream): Input video stream.
            min_r (int): set min blur radius (from 0 to 254)

                Defaults to 0.
            max_r (int): set max blur radius (from 1 to 255)

                Defaults to 8.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="varblur",
            inputs=[self, radius_stream],
            named_arguments={
                "min_r": min_r,
                "max_r": max_r,
                "planes": planes,
            },
        )[0]

    def vectorscope(
        self,
        mode: Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | int
        | None = None,
        m: Literal["gray", "tint", "color", "color2", "color3", "color4", "color5"]
        | int
        | None = None,
        x: int | None = None,
        y: int | None = None,
        intensity: float | None = None,
        i: float | None = None,
        envelope: Literal["none", "instant", "peak", "peak+instant"]
        | int
        | None = None,
        e: Literal["none", "instant", "peak", "peak+instant"] | int | None = None,
        graticule: Literal["none", "green", "color", "invert"] | int | None = None,
        g: Literal["none", "green", "color", "invert"] | int | None = None,
        opacity: float | None = None,
        o: float | None = None,
        flags: Literal["white", "black", "name"] | None = None,
        f: Literal["white", "black", "name"] | None = None,
        bgopacity: float | None = None,
        b: float | None = None,
        lthreshold: float | None = None,
        l: float | None = None,
        hthreshold: float | None = None,
        h: float | None = None,
        colorspace: Literal["auto", "601", "709"] | int | None = None,
        c: Literal["auto", "601", "709"] | int | None = None,
        tint0: float | None = None,
        t0: float | None = None,
        tint1: float | None = None,
        t1: float | None = None,
    ) -> "Stream":
        """Video vectorscope.

        Args:
            mode (int | str): set vectorscope mode (from 0 to 5)

                Allowed values:
                    * gray
                    * tint
                    * color
                    * color2
                    * color3
                    * color4
                    * color5

                Defaults to gray.
            m (int | str): set vectorscope mode (from 0 to 5)

                Allowed values:
                    * gray
                    * tint
                    * color
                    * color2
                    * color3
                    * color4
                    * color5

                Defaults to gray.
            x (int): set color component on X axis (from 0 to 2)

                Defaults to 1.
            y (int): set color component on Y axis (from 0 to 2)

                Defaults to 2.
            intensity (float): set intensity (from 0 to 1)

                Defaults to 0.004.
            i (float): set intensity (from 0 to 1)

                Defaults to 0.004.
            envelope (int | str): set envelope (from 0 to 3)

                Allowed values:
                    * none
                    * instant
                    * peak
                    * peak+instant

                Defaults to none.
            e (int | str): set envelope (from 0 to 3)

                Allowed values:
                    * none
                    * instant
                    * peak
                    * peak+instant

                Defaults to none.
            graticule (int | str): set graticule (from 0 to 3)

                Allowed values:
                    * none
                    * green
                    * color
                    * invert

                Defaults to none.
            g (int | str): set graticule (from 0 to 3)

                Allowed values:
                    * none
                    * green
                    * color
                    * invert

                Defaults to none.
            opacity (float): set graticule opacity (from 0 to 1)

                Defaults to 0.75.
            o (float): set graticule opacity (from 0 to 1)

                Defaults to 0.75.
            flags (str): set graticule flags

                Allowed values:
                    * white: white point
                    * black: black point
                    * name: point name

                Defaults to name.
            f (str): set graticule flags

                Allowed values:
                    * white: white point
                    * black: black point
                    * name: point name

                Defaults to name.
            bgopacity (float): set background opacity (from 0 to 1)

                Defaults to 0.3.
            b (float): set background opacity (from 0 to 1)

                Defaults to 0.3.
            lthreshold (float): set low threshold (from 0 to 1)

                Defaults to 0.
            l (float): set low threshold (from 0 to 1)

                Defaults to 0.
            hthreshold (float): set high threshold (from 0 to 1)

                Defaults to 1.
            h (float): set high threshold (from 0 to 1)

                Defaults to 1.
            colorspace (int | str): set colorspace (from 0 to 2)

                Allowed values:
                    * auto
                    * 601
                    * 709

                Defaults to auto.
            c (int | str): set colorspace (from 0 to 2)

                Allowed values:
                    * auto
                    * 601
                    * 709

                Defaults to auto.
            tint0 (float): set 1st tint (from -1 to 1)

                Defaults to 0.
            t0 (float): set 1st tint (from -1 to 1)

                Defaults to 0.
            tint1 (float): set 2nd tint (from -1 to 1)

                Defaults to 0.
            t1 (float): set 2nd tint (from -1 to 1)

                Defaults to 0.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vectorscope",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "x": x,
                "y": y,
                "intensity": intensity,
                "i": i,
                "envelope": envelope,
                "e": e,
                "graticule": graticule,
                "g": g,
                "opacity": opacity,
                "o": o,
                "flags": flags,
                "f": f,
                "bgopacity": bgopacity,
                "b": b,
                "lthreshold": lthreshold,
                "l": l,
                "hthreshold": hthreshold,
                "h": h,
                "colorspace": colorspace,
                "c": c,
                "tint0": tint0,
                "t0": t0,
                "tint1": tint1,
                "t1": t1,
            },
        )[0]

    def vflip(
        self,
    ) -> "Stream":
        """Flip the input video vertically.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vflip", inputs=[self], named_arguments={}
        )[0]

    def vfrdet(
        self,
    ) -> "Stream":
        """Variable frame rate detect filter.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vfrdet", inputs=[self], named_arguments={}
        )[0]

    def vibrance(
        self,
        intensity: float | None = None,
        rbal: float | None = None,
        gbal: float | None = None,
        bbal: float | None = None,
        rlum: float | None = None,
        glum: float | None = None,
        blum: float | None = None,
        alternate: bool | None = None,
    ) -> "Stream":
        """Boost or alter saturation.

        Args:
            intensity (float): set the intensity value (from -2 to 2)

                Defaults to 0.
            rbal (float): set the red balance value (from -10 to 10)

                Defaults to 1.
            gbal (float): set the green balance value (from -10 to 10)

                Defaults to 1.
            bbal (float): set the blue balance value (from -10 to 10)

                Defaults to 1.
            rlum (float): set the red luma coefficient (from 0 to 1)

                Defaults to 0.212656.
            glum (float): set the green luma coefficient (from 0 to 1)

                Defaults to 0.715158.
            blum (float): set the blue luma coefficient (from 0 to 1)

                Defaults to 0.072186.
            alternate (bool): use alternate colors

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vibrance",
            inputs=[self],
            named_arguments={
                "intensity": intensity,
                "rbal": rbal,
                "gbal": gbal,
                "bbal": bbal,
                "rlum": rlum,
                "glum": glum,
                "blum": blum,
                "alternate": alternate,
            },
        )[0]

    def vibrato(self, f: float | None = None, d: float | None = None) -> "Stream":
        """Apply vibrato effect.

        Args:
            f (float): set frequency in hertz (from 0.1 to 20000)

                Defaults to 5.
            d (float): set depth as percentage (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vibrato",
            inputs=[self],
            named_arguments={
                "f": f,
                "d": d,
            },
        )[0]

    def vidstabdetect(
        self,
        result: str | None = None,
        shakiness: int | None = None,
        accuracy: int | None = None,
        stepsize: int | None = None,
        mincontrast: float | None = None,
        show: int | None = None,
        tripod: int | None = None,
        fileformat: Literal["ascii", "binary"] | int | None = None,
    ) -> "Stream":
        """Extract relative transformations, pass 1 of 2 for stabilization (see vidstabtransform for pass 2).

        Args:
            result (str): path to the file used to write the transforms

                Defaults to transforms.trf.
            shakiness (int): how shaky is the video and how quick is the camera? 1: little (fast) 10: very strong/quick (slow) (from 1 to 10)

                Defaults to 5.
            accuracy (int): (>=shakiness) 1: low 15: high (slow) (from 1 to 15)

                Defaults to 15.
            stepsize (int): region around minimum is scanned with 1 pixel resolution (from 1 to 32)

                Defaults to 6.
            mincontrast (float): below this contrast a field is discarded (0-1) (from 0 to 1)

                Defaults to 0.25.
            show (int): 0: draw nothing; 1,2: show fields and transforms (from 0 to 2)

                Defaults to 0.
            tripod (int): virtual tripod mode (if >0): motion is compared to a reference reference frame (frame # is the value) (from 0 to INT_MAX)

                Defaults to 0.
            fileformat (int | str): transforms data file format (from 1 to 2)

                Allowed values:
                    * ascii: ASCII text
                    * binary: binary

                Defaults to binary.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vidstabdetect",
            inputs=[self],
            named_arguments={
                "result": result,
                "shakiness": shakiness,
                "accuracy": accuracy,
                "stepsize": stepsize,
                "mincontrast": mincontrast,
                "show": show,
                "tripod": tripod,
                "fileformat": fileformat,
            },
        )[0]

    def vidstabtransform(
        self,
        input: str | None = None,
        smoothing: int | None = None,
        optalgo: Literal["opt", "gauss", "avg"] | int | None = None,
        maxshift: int | None = None,
        maxangle: float | None = None,
        crop: Literal["keep", "black"] | int | None = None,
        invert: int | None = None,
        relative: int | None = None,
        zoom: float | None = None,
        optzoom: int | None = None,
        zoomspeed: float | None = None,
        interpol: Literal["no", "linear", "bilinear", "bicubic"] | int | None = None,
        tripod: bool | None = None,
        debug: bool | None = None,
    ) -> "Stream":
        """Transform the frames, pass 2 of 2 for stabilization (see vidstabdetect for pass 1).

        Args:
            input (str): set path to the file storing the transforms

                Defaults to transforms.trf.
            smoothing (int): set number of frames*2 + 1 used for lowpass filtering (from 0 to 1000)

                Defaults to 15.
            optalgo (int | str): set camera path optimization algo (from 0 to 2)

                Allowed values:
                    * opt: global optimization
                    * gauss: gaussian kernel
                    * avg: simple averaging on motion

                Defaults to opt.
            maxshift (int): set maximal number of pixels to translate image (from -1 to 500)

                Defaults to -1.
            maxangle (float): set maximal angle in rad to rotate image (from -1 to 3.14)

                Defaults to -1.
            crop (int | str): set cropping mode (from 0 to 1)

                Allowed values:
                    * keep: keep border
                    * black: black border

                Defaults to keep.
            invert (int): invert transforms (from 0 to 1)

                Defaults to 0.
            relative (int): consider transforms as relative (from 0 to 1)

                Defaults to 1.
            zoom (float): set percentage to zoom (>0: zoom in, <0: zoom out (from -100 to 100)

                Defaults to 0.
            optzoom (int): set optimal zoom (0: nothing, 1: optimal static zoom, 2: optimal dynamic zoom) (from 0 to 2)

                Defaults to 1.
            zoomspeed (float): for adative zoom: percent to zoom maximally each frame (from 0 to 5)

                Defaults to 0.25.
            interpol (int | str): set type of interpolation (from 0 to 3)

                Allowed values:
                    * no: no interpolation
                    * linear: linear (horizontal)
                    * bilinear: bi-linear
                    * bicubic: bi-cubic

                Defaults to bilinear.
            tripod (bool): enable virtual tripod mode (same as relative=0:smoothing=0)

                Defaults to false.
            debug (bool): enable debug mode and writer global motions information to file

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vidstabtransform",
            inputs=[self],
            named_arguments={
                "input": input,
                "smoothing": smoothing,
                "optalgo": optalgo,
                "maxshift": maxshift,
                "maxangle": maxangle,
                "crop": crop,
                "invert": invert,
                "relative": relative,
                "zoom": zoom,
                "optzoom": optzoom,
                "zoomspeed": zoomspeed,
                "interpol": interpol,
                "tripod": tripod,
                "debug": debug,
            },
        )[0]

    def vif(self, reference_stream: "Stream") -> "Stream":
        """Calculate the VIF between two video streams.

        Args:
            reference_stream (Stream): Input video stream.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vif", inputs=[self, reference_stream], named_arguments={}
        )[0]

    def vignette(
        self,
        angle: str | None = None,
        a: str | None = None,
        x0: str | None = None,
        y0: str | None = None,
        mode: Literal["forward", "backward"] | int | None = None,
        eval: Literal["init", "frame"] | int | None = None,
        dither: bool | None = None,
        aspect: str | None = None,
    ) -> "Stream":
        """Make or reverse a vignette effect.

        Args:
            angle (str): set lens angle

                Defaults to PI/5.
            a (str): set lens angle

                Defaults to PI/5.
            x0 (str): set circle center position on x-axis

                Defaults to w/2.
            y0 (str): set circle center position on y-axis

                Defaults to h/2.
            mode (int | str): set forward/backward mode (from 0 to 1)

                Allowed values:
                    * forward
                    * backward

                Defaults to forward.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * init: eval expressions once during initialization
                    * frame: eval expressions for each frame

                Defaults to init.
            dither (bool): set dithering

                Defaults to true.
            aspect (str): set aspect ratio (from 0 to DBL_MAX)

                Defaults to 1/1.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vignette",
            inputs=[self],
            named_arguments={
                "angle": angle,
                "a": a,
                "x0": x0,
                "y0": y0,
                "mode": mode,
                "eval": eval,
                "dither": dither,
                "aspect": aspect,
            },
        )[0]

    def virtualbass(
        self, cutoff: float | None = None, strength: float | None = None
    ) -> "Stream":
        """Audio Virtual Bass.

        Args:
            cutoff (float): set virtual bass cutoff (from 100 to 500)

                Defaults to 250.
            strength (float): set virtual bass strength (from 0.5 to 3)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="virtualbass",
            inputs=[self],
            named_arguments={
                "cutoff": cutoff,
                "strength": strength,
            },
        )[0]

    def vmafmotion(self, stats_file: str | None = None) -> "Stream":
        """Calculate the VMAF Motion score.

        Args:
            stats_file (str): Set file where to store per-frame difference information


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vmafmotion",
            inputs=[self],
            named_arguments={
                "stats_file": stats_file,
            },
        )[0]

    def volume(
        self,
        volume: str | None = None,
        precision: Literal["fixed", "float", "double"] | int | None = None,
        eval: Literal["once", "frame"] | int | None = None,
        replaygain: Literal["drop", "ignore", "track", "album"] | int | None = None,
        replaygain_preamp: float | None = None,
        replaygain_noclip: bool | None = None,
    ) -> "Stream":
        """Change input volume.

        Args:
            volume (str): set volume adjustment expression

                Defaults to 1.0.
            precision (int | str): select mathematical precision (from 0 to 2)

                Allowed values:
                    * fixed: select 8-bit fixed-point
                    * float: select 32-bit floating-point
                    * double: select 64-bit floating-point

                Defaults to float.
            eval (int | str): specify when to evaluate expressions (from 0 to 1)

                Allowed values:
                    * once: eval volume expression once
                    * frame: eval volume expression per-frame

                Defaults to once.
            replaygain (int | str): Apply replaygain side data when present (from 0 to 3)

                Allowed values:
                    * drop: replaygain side data is dropped
                    * ignore: replaygain side data is ignored
                    * track: track gain is preferred
                    * album: album gain is preferred

                Defaults to drop.
            replaygain_preamp (float): Apply replaygain pre-amplification (from -15 to 15)

                Defaults to 0.
            replaygain_noclip (bool): Apply replaygain clipping prevention

                Defaults to true.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="volume",
            inputs=[self],
            named_arguments={
                "volume": volume,
                "precision": precision,
                "eval": eval,
                "replaygain": replaygain,
                "replaygain_preamp": replaygain_preamp,
                "replaygain_noclip": replaygain_noclip,
            },
        )[0]

    def volumedetect(
        self,
    ) -> "Stream":
        """Detect audio volume.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="volumedetect", inputs=[self], named_arguments={}
        )[0]

    def vstack(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        shortest: bool | None = None,
    ) -> "Stream":
        """Stack video inputs vertically.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): set number of inputs (from 2 to INT_MAX)

                Defaults to 2.
            shortest (bool): force termination when the shortest input terminates

                Defaults to false.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="vstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "shortest": shortest,
            },
        )[0]

    def w3fdif(
        self,
        filter: Literal["simple", "complex"] | int | None = None,
        mode: Literal["frame", "field"] | int | None = None,
        parity: Literal["tff", "bff", "auto"] | int | None = None,
        deint: Literal["all", "interlaced"] | int | None = None,
    ) -> "Stream":
        """Apply Martin Weston three field deinterlace.

        Args:
            filter (int | str): specify the filter (from 0 to 1)

                Allowed values:
                    * simple
                    * complex

                Defaults to complex.
            mode (int | str): specify the interlacing mode (from 0 to 1)

                Allowed values:
                    * frame: send one frame for each frame
                    * field: send one frame for each field

                Defaults to field.
            parity (int | str): specify the assumed picture field parity (from -1 to 1)

                Allowed values:
                    * tff: assume top field first
                    * bff: assume bottom field first
                    * auto: auto detect parity

                Defaults to auto.
            deint (int | str): specify which frames to deinterlace (from 0 to 1)

                Allowed values:
                    * all: deinterlace all frames
                    * interlaced: only deinterlace frames marked as interlaced

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="w3fdif",
            inputs=[self],
            named_arguments={
                "filter": filter,
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def waveform(
        self,
        mode: Literal["row", "column"] | int | None = None,
        m: Literal["row", "column"] | int | None = None,
        intensity: float | None = None,
        i: float | None = None,
        mirror: bool | None = None,
        r: bool | None = None,
        display: Literal["overlay", "stack", "parade"] | int | None = None,
        d: Literal["overlay", "stack", "parade"] | int | None = None,
        components: int | None = None,
        c: int | None = None,
        envelope: Literal["none", "instant", "peak", "peak+instant"]
        | int
        | None = None,
        e: Literal["none", "instant", "peak", "peak+instant"] | int | None = None,
        filter: Literal[
            "lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"
        ]
        | int
        | None = None,
        f: Literal[
            "lowpass", "flat", "aflat", "chroma", "color", "acolor", "xflat", "yflat"
        ]
        | int
        | None = None,
        graticule: Literal["none", "green", "orange", "invert"] | int | None = None,
        g: Literal["none", "green", "orange", "invert"] | int | None = None,
        opacity: float | None = None,
        o: float | None = None,
        flags: Literal["numbers", "dots"] | None = None,
        fl: Literal["numbers", "dots"] | None = None,
        scale: Literal["digital", "millivolts", "ire"] | int | None = None,
        s: Literal["digital", "millivolts", "ire"] | int | None = None,
        bgopacity: float | None = None,
        b: float | None = None,
        tint0: float | None = None,
        t0: float | None = None,
        tint1: float | None = None,
        t1: float | None = None,
        fitmode: Literal["none", "size"] | int | None = None,
        fm: Literal["none", "size"] | int | None = None,
        input: Literal["all", "first"] | int | None = None,
    ) -> "Stream":
        """Video waveform monitor.

        Args:
            mode (int | str): set mode (from 0 to 1)

                Allowed values:
                    * row
                    * column

                Defaults to column.
            m (int | str): set mode (from 0 to 1)

                Allowed values:
                    * row
                    * column

                Defaults to column.
            intensity (float): set intensity (from 0 to 1)

                Defaults to 0.04.
            i (float): set intensity (from 0 to 1)

                Defaults to 0.04.
            mirror (bool): set mirroring

                Defaults to true.
            r (bool): set mirroring

                Defaults to true.
            display (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * stack
                    * parade

                Defaults to stack.
            d (int | str): set display mode (from 0 to 2)

                Allowed values:
                    * overlay
                    * stack
                    * parade

                Defaults to stack.
            components (int): set components to display (from 1 to 15)

                Defaults to 1.
            c (int): set components to display (from 1 to 15)

                Defaults to 1.
            envelope (int | str): set envelope to display (from 0 to 3)

                Allowed values:
                    * none
                    * instant
                    * peak
                    * peak+instant

                Defaults to none.
            e (int | str): set envelope to display (from 0 to 3)

                Allowed values:
                    * none
                    * instant
                    * peak
                    * peak+instant

                Defaults to none.
            filter (int | str): set filter (from 0 to 7)

                Allowed values:
                    * lowpass
                    * flat
                    * aflat
                    * chroma
                    * color
                    * acolor
                    * xflat
                    * yflat

                Defaults to lowpass.
            f (int | str): set filter (from 0 to 7)

                Allowed values:
                    * lowpass
                    * flat
                    * aflat
                    * chroma
                    * color
                    * acolor
                    * xflat
                    * yflat

                Defaults to lowpass.
            graticule (int | str): set graticule (from 0 to 3)

                Allowed values:
                    * none
                    * green
                    * orange
                    * invert

                Defaults to none.
            g (int | str): set graticule (from 0 to 3)

                Allowed values:
                    * none
                    * green
                    * orange
                    * invert

                Defaults to none.
            opacity (float): set graticule opacity (from 0 to 1)

                Defaults to 0.75.
            o (float): set graticule opacity (from 0 to 1)

                Defaults to 0.75.
            flags (str): set graticule flags

                Allowed values:
                    * numbers: numbers
                    * dots: dots instead of lines

                Defaults to numbers.
            fl (str): set graticule flags

                Allowed values:
                    * numbers: numbers
                    * dots: dots instead of lines

                Defaults to numbers.
            scale (int | str): set scale (from 0 to 2)

                Allowed values:
                    * digital
                    * millivolts
                    * ire

                Defaults to digital.
            s (int | str): set scale (from 0 to 2)

                Allowed values:
                    * digital
                    * millivolts
                    * ire

                Defaults to digital.
            bgopacity (float): set background opacity (from 0 to 1)

                Defaults to 0.75.
            b (float): set background opacity (from 0 to 1)

                Defaults to 0.75.
            tint0 (float): set 1st tint (from -1 to 1)

                Defaults to 0.
            t0 (float): set 1st tint (from -1 to 1)

                Defaults to 0.
            tint1 (float): set 2nd tint (from -1 to 1)

                Defaults to 0.
            t1 (float): set 2nd tint (from -1 to 1)

                Defaults to 0.
            fitmode (int | str): set fit mode (from 0 to 1)

                Allowed values:
                    * none
                    * size

                Defaults to none.
            fm (int | str): set fit mode (from 0 to 1)

                Allowed values:
                    * none
                    * size

                Defaults to none.
            input (int | str): set input formats selection (from 0 to 1)

                Allowed values:
                    * all: try to select from all available formats
                    * first: pick first available format

                Defaults to first.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="waveform",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "m": m,
                "intensity": intensity,
                "i": i,
                "mirror": mirror,
                "r": r,
                "display": display,
                "d": d,
                "components": components,
                "c": c,
                "envelope": envelope,
                "e": e,
                "filter": filter,
                "f": f,
                "graticule": graticule,
                "g": g,
                "opacity": opacity,
                "o": o,
                "flags": flags,
                "fl": fl,
                "scale": scale,
                "s": s,
                "bgopacity": bgopacity,
                "b": b,
                "tint0": tint0,
                "t0": t0,
                "tint1": tint1,
                "t1": t1,
                "fitmode": fitmode,
                "fm": fm,
                "input": input,
            },
        )[0]

    def weave(
        self, first_field: Literal["top", "t", "bottom", "b"] | int | None = None
    ) -> "Stream":
        """Weave input video fields into frames.

        Args:
            first_field (int | str): set first field (from 0 to 1)

                Allowed values:
                    * top: set top field first
                    * t: set top field first
                    * bottom: set bottom field first
                    * b: set bottom field first

                Defaults to top.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="weave",
            inputs=[self],
            named_arguments={
                "first_field": first_field,
            },
        )[0]

    def xbr(self, n: int | None = None) -> "Stream":
        """Scale the input using xBR algorithm.

        Args:
            n (int): set scale factor (from 2 to 4)

                Defaults to 3.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xbr",
            inputs=[self],
            named_arguments={
                "n": n,
            },
        )[0]

    def xcorrelate(
        self,
        secondary_stream: "Stream",
        planes: int | None = None,
        secondary: Literal["first", "all"] | int | None = None,
    ) -> "Stream":
        """Cross-correlate first video stream with second video stream.

        Args:
            secondary_stream (Stream): Input video stream.
            planes (int): set planes to cross-correlate (from 0 to 15)

                Defaults to 7.
            secondary (int | str): when to process secondary frame (from 0 to 1)

                Allowed values:
                    * first: process only first secondary frame, ignore rest
                    * all: process all secondary frames

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xcorrelate",
            inputs=[self, secondary_stream],
            named_arguments={
                "planes": planes,
                "secondary": secondary,
            },
        )[0]

    def xfade(
        self,
        xfade_stream: "Stream",
        transition: Literal[
            "custom",
            "fade",
            "wipeleft",
            "wiperight",
            "wipeup",
            "wipedown",
            "slideleft",
            "slideright",
            "slideup",
            "slidedown",
            "circlecrop",
            "rectcrop",
            "distance",
            "fadeblack",
            "fadewhite",
            "radial",
            "smoothleft",
            "smoothright",
            "smoothup",
            "smoothdown",
            "circleopen",
            "circleclose",
            "vertopen",
            "vertclose",
            "horzopen",
            "horzclose",
            "dissolve",
            "pixelize",
            "diagtl",
            "diagtr",
            "diagbl",
            "diagbr",
            "hlslice",
            "hrslice",
            "vuslice",
            "vdslice",
            "hblur",
            "fadegrays",
            "wipetl",
            "wipetr",
            "wipebl",
            "wipebr",
            "squeezeh",
            "squeezev",
            "zoomin",
            "fadefast",
            "fadeslow",
            "hlwind",
            "hrwind",
            "vuwind",
            "vdwind",
            "coverleft",
            "coverright",
            "coverup",
            "coverdown",
            "revealleft",
            "revealright",
            "revealup",
            "revealdown",
        ]
        | int
        | None = None,
        duration: str | None = None,
        offset: str | None = None,
        expr: str | None = None,
    ) -> "Stream":
        """Cross fade one video with another video.

        Args:
            xfade_stream (Stream): Input video stream.
            transition (int | str): set cross fade transition (from -1 to 57)

                Allowed values:
                    * custom: custom transition
                    * fade: fade transition
                    * wipeleft: wipe left transition
                    * wiperight: wipe right transition
                    * wipeup: wipe up transition
                    * wipedown: wipe down transition
                    * slideleft: slide left transition
                    * slideright: slide right transition
                    * slideup: slide up transition
                    * slidedown: slide down transition
                    * circlecrop: circle crop transition
                    * rectcrop: rect crop transition
                    * distance: distance transition
                    * fadeblack: fadeblack transition
                    * fadewhite: fadewhite transition
                    * radial: radial transition
                    * smoothleft: smoothleft transition
                    * smoothright: smoothright transition
                    * smoothup: smoothup transition
                    * smoothdown: smoothdown transition
                    * circleopen: circleopen transition
                    * circleclose: circleclose transition
                    * vertopen: vert open transition
                    * vertclose: vert close transition
                    * horzopen: horz open transition
                    * horzclose: horz close transition
                    * dissolve: dissolve transition
                    * pixelize: pixelize transition
                    * diagtl: diag tl transition
                    * diagtr: diag tr transition
                    * diagbl: diag bl transition
                    * diagbr: diag br transition
                    * hlslice: hl slice transition
                    * hrslice: hr slice transition
                    * vuslice: vu slice transition
                    * vdslice: vd slice transition
                    * hblur: hblur transition
                    * fadegrays: fadegrays transition
                    * wipetl: wipe tl transition
                    * wipetr: wipe tr transition
                    * wipebl: wipe bl transition
                    * wipebr: wipe br transition
                    * squeezeh: squeeze h transition
                    * squeezev: squeeze v transition
                    * zoomin: zoom in transition
                    * fadefast: fast fade transition
                    * fadeslow: slow fade transition
                    * hlwind: hl wind transition
                    * hrwind: hr wind transition
                    * vuwind: vu wind transition
                    * vdwind: vd wind transition
                    * coverleft: cover left transition
                    * coverright: cover right transition
                    * coverup: cover up transition
                    * coverdown: cover down transition
                    * revealleft: reveal left transition
                    * revealright: reveal right transition
                    * revealup: reveal up transition
                    * revealdown: reveal down transition

                Defaults to fade.
            duration (str): set cross fade duration

                Defaults to 1.
            offset (str): set cross fade start relative to first input stream

                Defaults to 0.
            expr (str): set expression for custom transition


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xfade",
            inputs=[self, xfade_stream],
            named_arguments={
                "transition": transition,
                "duration": duration,
                "offset": offset,
                "expr": expr,
            },
        )[0]

    def xmedian(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        planes: int | None = None,
        percentile: float | None = None,
    ) -> "Stream":
        """Pick median pixels from several video inputs.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): set number of inputs (from 3 to 255)

                Defaults to 3.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 15.
            percentile (float): set percentile (from 0 to 1)

                Defaults to 0.5.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xmedian",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "planes": planes,
                "percentile": percentile,
            },
        )[0]

    def xpsnr(
        self,
        reference_stream: "Stream",
        stats_file: str | None = None,
        f: str | None = None,
    ) -> "Stream":
        """Calculate the extended perceptually weighted peak signal-to-noise ratio (XPSNR) between two video streams.

        Args:
            reference_stream (Stream): Input video stream.
            stats_file (str): Set file where to store per-frame XPSNR information

            f (str): Set file where to store per-frame XPSNR information


        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xpsnr",
            inputs=[self, reference_stream],
            named_arguments={
                "stats_file": stats_file,
                "f": f,
            },
        )[0]

    def xstack(
        self,
        *streams: "Stream",
        inputs: int | None = None,
        layout: str | None = None,
        grid: str | None = None,
        shortest: bool | None = None,
        fill: str | None = None,
    ) -> "Stream":
        """Stack video inputs into custom layout.

        Args:
            *streams (Stream): One or more input streams.
            inputs (int): set number of inputs (from 2 to INT_MAX)

                Defaults to 2.
            layout (str): set custom layout

            grid (str): set fixed size grid layout

            shortest (bool): force termination when the shortest input terminates

                Defaults to false.
            fill (str): set the color for unused pixels

                Defaults to none.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="xstack",
            inputs=[self, *streams],
            named_arguments={
                "inputs": inputs,
                "layout": layout,
                "grid": grid,
                "shortest": shortest,
                "fill": fill,
            },
        )[0]

    def yadif(
        self,
        mode: Literal[
            "send_frame", "send_field", "send_frame_nospatial", "send_field_nospatial"
        ]
        | int
        | None = None,
        parity: Literal["tff", "bff", "auto"] | int | None = None,
        deint: Literal["all", "interlaced"] | int | None = None,
    ) -> "Stream":
        """Deinterlace the input image.

        Args:
            mode (int | str): specify the interlacing mode (from 0 to 3)

                Allowed values:
                    * send_frame: send one frame for each frame
                    * send_field: send one frame for each field
                    * send_frame_nospatial: send one frame for each frame, but skip spatial interlacing check
                    * send_field_nospatial: send one frame for each field, but skip spatial interlacing check

                Defaults to send_frame.
            parity (int | str): specify the assumed picture field parity (from -1 to 1)

                Allowed values:
                    * tff: assume top field first
                    * bff: assume bottom field first
                    * auto: auto detect parity

                Defaults to auto.
            deint (int | str): specify which frames to deinterlace (from 0 to 1)

                Allowed values:
                    * all: deinterlace all frames
                    * interlaced: only deinterlace frames marked as interlaced

                Defaults to all.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="yadif",
            inputs=[self],
            named_arguments={
                "mode": mode,
                "parity": parity,
                "deint": deint,
            },
        )[0]

    def yaepblur(
        self,
        radius: int | None = None,
        r: int | None = None,
        planes: int | None = None,
        p: int | None = None,
        sigma: int | None = None,
        s: int | None = None,
    ) -> "Stream":
        """Yet another edge preserving blur filter.

        Args:
            radius (int): set window radius (from 0 to INT_MAX)

                Defaults to 3.
            r (int): set window radius (from 0 to INT_MAX)

                Defaults to 3.
            planes (int): set planes to filter (from 0 to 15)

                Defaults to 1.
            p (int): set planes to filter (from 0 to 15)

                Defaults to 1.
            sigma (int): set blur strength (from 1 to INT_MAX)

                Defaults to 128.
            s (int): set blur strength (from 1 to INT_MAX)

                Defaults to 128.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="yaepblur",
            inputs=[self],
            named_arguments={
                "radius": radius,
                "r": r,
                "planes": planes,
                "p": p,
                "sigma": sigma,
                "s": s,
            },
        )[0]

    def zmq(self, bind_address: str | None = None, b: str | None = None) -> "Stream":
        """Receive commands through ZMQ and broker them to filters.

        Args:
            bind_address (str): set bind address

                Defaults to tcp://*:5555.
            b (str): set bind address

                Defaults to tcp://*:5555.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="zmq",
            inputs=[self],
            named_arguments={
                "bind_address": bind_address,
                "b": b,
            },
        )[0]

    def zoompan(
        self,
        zoom: str | None = None,
        z: str | None = None,
        x: str | None = None,
        y: str | None = None,
        d: str | None = None,
        s: str | None = None,
        fps: str | None = None,
    ) -> "Stream":
        """Apply Zoom & Pan effect.

        Args:
            zoom (str): set the zoom expression

                Defaults to 1.
            z (str): set the zoom expression

                Defaults to 1.
            x (str): set the x expression

                Defaults to 0.
            y (str): set the y expression

                Defaults to 0.
            d (str): set the duration expression

                Defaults to 90.
            s (str): set the output image size

                Defaults to hd720.
            fps (str): set the output framerate

                Defaults to 25.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="zoompan",
            inputs=[self],
            named_arguments={
                "zoom": zoom,
                "z": z,
                "x": x,
                "y": y,
                "d": d,
                "s": s,
                "fps": fps,
            },
        )[0]

    def zscale(
        self,
        w: str | None = None,
        width: str | None = None,
        h: str | None = None,
        height: str | None = None,
        size: str | None = None,
        s: str | None = None,
        dither: Literal["none", "ordered", "random", "error_diffusion"]
        | int
        | None = None,
        d: Literal["none", "ordered", "random", "error_diffusion"] | int | None = None,
        filter: Literal[
            "point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"
        ]
        | int
        | None = None,
        f: Literal["point", "bilinear", "bicubic", "spline16", "spline36", "lanczos"]
        | int
        | None = None,
        out_range: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        range: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        r: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        primaries: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        p: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        transfer: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int
        | None = None,
        t: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int
        | None = None,
        matrix: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int
        | None = None,
        m: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int
        | None = None,
        in_range: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        rangein: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        rin: Literal["input", "limited", "full", "unknown", "tv", "pc"]
        | int
        | None = None,
        primariesin: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        pin: Literal[
            "input",
            "709",
            "unspecified",
            "170m",
            "240m",
            "2020",
            "unknown",
            "bt709",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "film",
            "bt2020",
            "smpte428",
            "smpte431",
            "smpte432",
            "jedec-p22",
            "ebu3213",
        ]
        | int
        | None = None,
        transferin: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int
        | None = None,
        tin: Literal[
            "input",
            "709",
            "unspecified",
            "601",
            "linear",
            "2020_10",
            "2020_12",
            "unknown",
            "bt470m",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "bt709",
            "linear",
            "log100",
            "log316",
            "bt2020-10",
            "bt2020-12",
            "smpte2084",
            "iec61966-2-4",
            "iec61966-2-1",
            "arib-std-b67",
        ]
        | int
        | None = None,
        matrixin: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int
        | None = None,
        min: Literal[
            "input",
            "709",
            "unspecified",
            "470bg",
            "170m",
            "2020_ncl",
            "2020_cl",
            "unknown",
            "gbr",
            "bt709",
            "fcc",
            "bt470bg",
            "smpte170m",
            "smpte240m",
            "ycgco",
            "bt2020nc",
            "bt2020c",
            "chroma-derived-nc",
            "chroma-derived-c",
            "ictcp",
        ]
        | int
        | None = None,
        chromal: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int
        | None = None,
        c: Literal["input", "left", "center", "topleft", "top", "bottomleft", "bottom"]
        | int
        | None = None,
        chromalin: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int
        | None = None,
        cin: Literal[
            "input", "left", "center", "topleft", "top", "bottomleft", "bottom"
        ]
        | int
        | None = None,
        npl: float | None = None,
        agamma: bool | None = None,
        param_a: float | None = None,
        param_b: float | None = None,
    ) -> "Stream":
        """Apply resizing, colorspace and bit depth conversion.

        Args:
            w (str): Output video width

            width (str): Output video width

            h (str): Output video height

            height (str): Output video height

            size (str): set video size

            s (str): set video size

            dither (int | str): set dither type (from 0 to 3)

                Allowed values:
                    * none
                    * ordered
                    * random
                    * error_diffusion

                Defaults to none.
            d (int | str): set dither type (from 0 to 3)

                Allowed values:
                    * none
                    * ordered
                    * random
                    * error_diffusion

                Defaults to none.
            filter (int | str): set filter type (from 0 to 5)

                Allowed values:
                    * point
                    * bilinear
                    * bicubic
                    * spline16
                    * spline36
                    * lanczos

                Defaults to bilinear.
            f (int | str): set filter type (from 0 to 5)

                Allowed values:
                    * point
                    * bilinear
                    * bicubic
                    * spline16
                    * spline36
                    * lanczos

                Defaults to bilinear.
            out_range (int | str): set color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            range (int | str): set color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            r (int | str): set color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            primaries (int | str): set color primaries (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 170m
                    * 240m
                    * 2020
                    * unknown
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to input.
            p (int | str): set color primaries (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 170m
                    * 240m
                    * 2020
                    * unknown
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to input.
            transfer (int | str): set transfer characteristic (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 601
                    * linear
                    * 2020_10
                    * 2020_12
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * bt709
                    * linear
                    * log100
                    * log316
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * iec61966-2-4
                    * iec61966-2-1
                    * arib-std-b67

                Defaults to input.
            t (int | str): set transfer characteristic (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 601
                    * linear
                    * 2020_10
                    * 2020_12
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * bt709
                    * linear
                    * log100
                    * log316
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * iec61966-2-4
                    * iec61966-2-1
                    * arib-std-b67

                Defaults to input.
            matrix (int | str): set colorspace matrix (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 470bg
                    * 170m
                    * 2020_ncl
                    * 2020_cl
                    * unknown
                    * gbr
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * bt2020nc
                    * bt2020c
                    * chroma-derived-nc
                    * chroma-derived-c
                    * ictcp

                Defaults to input.
            m (int | str): set colorspace matrix (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 470bg
                    * 170m
                    * 2020_ncl
                    * 2020_cl
                    * unknown
                    * gbr
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * bt2020nc
                    * bt2020c
                    * chroma-derived-nc
                    * chroma-derived-c
                    * ictcp

                Defaults to input.
            in_range (int | str): set input color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            rangein (int | str): set input color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            rin (int | str): set input color range (from -1 to 1)

                Allowed values:
                    * input
                    * limited
                    * full
                    * unknown
                    * tv
                    * pc

                Defaults to input.
            primariesin (int | str): set input color primaries (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 170m
                    * 240m
                    * 2020
                    * unknown
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to input.
            pin (int | str): set input color primaries (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 170m
                    * 240m
                    * 2020
                    * unknown
                    * bt709
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * film
                    * bt2020
                    * smpte428
                    * smpte431
                    * smpte432
                    * jedec-p22
                    * ebu3213

                Defaults to input.
            transferin (int | str): set input transfer characteristic (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 601
                    * linear
                    * 2020_10
                    * 2020_12
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * bt709
                    * linear
                    * log100
                    * log316
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * iec61966-2-4
                    * iec61966-2-1
                    * arib-std-b67

                Defaults to input.
            tin (int | str): set input transfer characteristic (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 601
                    * linear
                    * 2020_10
                    * 2020_12
                    * unknown
                    * bt470m
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * bt709
                    * linear
                    * log100
                    * log316
                    * bt2020-10
                    * bt2020-12
                    * smpte2084
                    * iec61966-2-4
                    * iec61966-2-1
                    * arib-std-b67

                Defaults to input.
            matrixin (int | str): set input colorspace matrix (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 470bg
                    * 170m
                    * 2020_ncl
                    * 2020_cl
                    * unknown
                    * gbr
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * bt2020nc
                    * bt2020c
                    * chroma-derived-nc
                    * chroma-derived-c
                    * ictcp

                Defaults to input.
            min (int | str): set input colorspace matrix (from -1 to INT_MAX)

                Allowed values:
                    * input
                    * 709
                    * unspecified
                    * 470bg
                    * 170m
                    * 2020_ncl
                    * 2020_cl
                    * unknown
                    * gbr
                    * bt709
                    * fcc
                    * bt470bg
                    * smpte170m
                    * smpte240m
                    * ycgco
                    * bt2020nc
                    * bt2020c
                    * chroma-derived-nc
                    * chroma-derived-c
                    * ictcp

                Defaults to input.
            chromal (int | str): set output chroma location (from -1 to 5)

                Allowed values:
                    * input
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to input.
            c (int | str): set output chroma location (from -1 to 5)

                Allowed values:
                    * input
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to input.
            chromalin (int | str): set input chroma location (from -1 to 5)

                Allowed values:
                    * input
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to input.
            cin (int | str): set input chroma location (from -1 to 5)

                Allowed values:
                    * input
                    * left
                    * center
                    * topleft
                    * top
                    * bottomleft
                    * bottom

                Defaults to input.
            npl (float): set nominal peak luminance (from 0 to DBL_MAX)

                Defaults to nan.
            agamma (bool): allow approximate gamma

                Defaults to true.
            param_a (float): parameter A, which is parameter "b" for bicubic, and the number of filter taps for lanczos (from -DBL_MAX to DBL_MAX)

                Defaults to nan.
            param_b (float): parameter B, which is parameter "c" for bicubic (from -DBL_MAX to DBL_MAX)

                Defaults to nan.

        Returns:
            "Stream": The output stream.
        """
        return self._apply_filter(
            filter_name="zscale",
            inputs=[self],
            named_arguments={
                "w": w,
                "width": width,
                "h": h,
                "height": height,
                "size": size,
                "s": s,
                "dither": dither,
                "d": d,
                "filter": filter,
                "f": f,
                "out_range": out_range,
                "range": range,
                "r": r,
                "primaries": primaries,
                "p": p,
                "transfer": transfer,
                "t": t,
                "matrix": matrix,
                "m": m,
                "in_range": in_range,
                "rangein": rangein,
                "rin": rin,
                "primariesin": primariesin,
                "pin": pin,
                "transferin": transferin,
                "tin": tin,
                "matrixin": matrixin,
                "min": min,
                "chromal": chromal,
                "c": c,
                "chromalin": chromalin,
                "cin": cin,
                "npl": npl,
                "agamma": agamma,
                "param_a": param_a,
                "param_b": param_b,
            },
        )[0]
